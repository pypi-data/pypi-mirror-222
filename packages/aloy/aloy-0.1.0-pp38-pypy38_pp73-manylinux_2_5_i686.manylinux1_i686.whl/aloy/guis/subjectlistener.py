# Copyright (C) 2023 Oliver Michael Kamperis
# Email: o.m.kamperis@gmail.com
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

"""
Module defining the subject-listener design pattern.

The subject-listener pattern is a middle ground between the observable-observer
and publisher-subscriber patterns. It is similar to the observable-observer in
that listeners are registered with a subject and are notified when the subject
changes. It is similar to the publisher-subscriber pattern in that listeners
can subscribe to specific fields of the subject. Unlike the observable-observer
pattern, listeners are notified only when a field they are subscribed to
changes, and are only sent the relevant information, greatly increasing the
sacalability of the pattern. Unlike the publisher-subscriber pattern, a
subject is not a global singleton, and the intended method is to sub-class
the subject class to create a new subject type containing the fields that
listeners can subscribe to.

Because the subject-listener pattern only updates listeners when a field
they are listening to changes, there is less generality to the pattern than
the observerable-observer pattern.
"""

import functools
import inspect
import logging
from collections import defaultdict, deque
from typing import Any, Callable, Concatenate, Final, ParamSpec, TypeVar, final

from aloy.concurrency.executors import AloyThreadPool
from aloy.concurrency.synchronization import SynchronizedMeta, sync
from aloy.datastructures.mappings import TwoWayMap

__copyright__ = "Copyright (C) 2023 Oliver Michael Kamperis"
__license__ = "GPL-3.0"

__all__ = (
    "Listener",
    "Subject",
    "call_on_field_change",
    "field",
    "field_change"
)


def __dir__() -> tuple[str, ...]:
    """Get the names of module attributes."""
    return __all__


def call_on_field_change(
    field_name: str
) -> Callable[
    [Callable[["Listener", "Subject", str, Any, Any], None]],
    Callable[["Listener", "Subject", str, Any, Any], None]
]:
    """Decorate a method to be called when a field changes."""
    def decorator(
        func: Callable[["Listener", "Subject", str, Any, Any], None]
    ) -> Callable[["Listener", "Subject", str, Any, Any], None]:
        func.__subject_field__ = field_name  # type: ignore
        return func
    return decorator


class Listener:
    def field_changed(
        self,
        source: "Subject",
        field_name: str,
        old_value: Any,
        new_value: Any
    ) -> None:
        return NotImplemented  # type: ignore


SP = ParamSpec("SP")
ST = TypeVar("ST")


def field(
    field_name: str | None = None,
    queue_size: int | None = None
) -> Callable[
    [Callable[Concatenate["Subject", SP], ST]],
    Callable[Concatenate["Subject", SP], ST]
]:
    """
    Decorate a field to be tracked by a Subject.

    The decorated method must have be callacble with no arguments and return
    the current value of the field.

    Parameters
    ----------
    `field_name: str | None = None` - The name of the field. If not given or
    None, the name of the method is used.

    `queue_size: int | None = None` - The size of the queue used to store
    values of the field. If not given or None, the field is not queued.
    """
    def decorator(
        func: Callable[Concatenate["Subject", SP], ST]
    ) -> Callable[Concatenate["Subject", SP], ST]:
        _field_name: str
        if field_name is None:
            _field_name = func.__name__
        else:
            _field_name = field_name
        func.__subject_field__ = _field_name  # type: ignore
        func.__queue_size__ = queue_size  # type: ignore
        return sync(lock="method", group_name=f"get:({_field_name})")(func)
    return decorator


def field_change(
    field_name: str | None = None
) -> Callable[
    [Callable[Concatenate["Subject", SP], ST]],
    Callable[Concatenate["Subject", SP], ST]
]:
    """
    Decorate a method to indicate that it changes a field.

    There are no restrictions on the method signature.

    A field with the same name must have been defined prior to this decorator
    being applied.

    Parameters
    ----------
    `field_name: str | None = None` - The name of the field. If not given or
    None, the name of the method is used.
    """
    def decorator(
        func: Callable[Concatenate["Subject", SP], ST]
    ) -> Callable[Concatenate["Subject", SP], ST]:
        _field_name: str
        if field_name is None:
            _field_name = func.__name__
        else:
            _field_name = field_name

        func.__subject_field_change__ = _field_name  # type: ignore

        # pylint: disable=protected-access
        @sync(lock="method", group_name=f"update:({_field_name})")
        @functools.wraps(func)
        def wrapper(self: "Subject", *args: Any, **kwargs: Any) -> Any:
            old_value = self.__get_field__(_field_name)
            func(self, *args, **kwargs)
            new_value = self.__get_field__(_field_name, new_value=True)
            if self.__is_queued_field__(_field_name):
                self.__update__(_field_name, old_value, new_value)
            elif old_value != new_value:
                self.__update__(_field_name, old_value, new_value)

        return wrapper
    return decorator


@final
class _SubjectSynchronizedMeta(SynchronizedMeta):
    """
    Synchronized metaclass for Subject.

    Gathers all fields and callbacks defined in the class namespace into the
    `__subject_fields__` attribute. This is a dictionary mapping field names to
    getter functions. Properties have their `fget` attribute pre-extracted.
    """

    def __new__(
        cls,
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any]
    ) -> type:
        """Create a new synchronized subject class."""
        _existing_subject_fields = namespace.get("__SUBJECT_FIELDS__")
        if _existing_subject_fields is None:
            _existing_subject_fields = {}
            namespace["__SUBJECT_FIELDS__"] = _existing_subject_fields
        _new_subject_fields = {}
        for attr in namespace.values():
            if isinstance(attr, property):
                _get_attr = attr.fget
                _set_attr = attr.fset
            else:
                _get_attr = attr
                _set_attr = attr
            if (_get_attr is not None
                    and hasattr(_get_attr, "__subject_field__")):
                _field_name = _get_attr.__subject_field__  # type: ignore
                _queue_size = _get_attr.__queue_size__  # type: ignore
                if _field_name in _existing_subject_fields:
                    raise ValueError(
                        f"Attribute {_get_attr.__name__} defined a field "
                        f"name '{_field_name}' which was already defined in a "
                        f"base class of {name}."
                    )
                if _field_name in _new_subject_fields:
                    raise ValueError(
                        f"Attribute {_get_attr.__name__} defined a field "
                        f"name '{_field_name}' which was already defined in "
                        f"the class {name}."
                    )
                _new_subject_fields[_field_name] = (_get_attr, _queue_size)
            if (_set_attr is not None
                    and hasattr(_set_attr, "__subject_field_change__")):
                _field_name = _set_attr \
                    .__subject_field_change__  # type: ignore
                if (_field_name not in _existing_subject_fields
                        and _field_name not in _new_subject_fields):
                    raise ValueError(
                        f"Attribute {_set_attr.__name__} defined as changing "
                        f"field '{_field_name}', but no field with that name "
                        f"was defined in (or a base class of) {name}."
                    )
        _existing_subject_fields.update(_new_subject_fields)

        return super().__new__(cls, name, bases, namespace)


_SUBJECT_DEFAULT_THREAD_POOL_EXECUTOR_MAX_WORKERS: Final[int] = 10
_SUBJECT_DEFAULT_THREAD_POOL_EXECUTOR_PROFILE: Final[bool] = False
_SUBJECT_DEFAULT_THREAD_POOL_EXECUTOR_LOG: Final[bool] = False


class Subject(metaclass=_SubjectSynchronizedMeta):
    """
    A subject is an object that can be observed by listeners.
    """

    __SUBJECT_LOGGER = logging.getLogger("Subject")
    __SUBJECT_FIELDS__: (
        dict[str, tuple[Callable[["Subject"], Any], bool]]
        | None
    ) = None

    __slots__ = {
        "__listeners": "The listeners registered with the subject.",
        "__callbacks": "The callbacks registered with the subject.",
        "__executor": "The thread pool executor used to update listeners.",
        "__queues": "The queues used to store values of queued fields."
    }

    def __init__(
        self,
        max_workers: int = _SUBJECT_DEFAULT_THREAD_POOL_EXECUTOR_MAX_WORKERS,
        profile: bool = _SUBJECT_DEFAULT_THREAD_POOL_EXECUTOR_PROFILE,
        log: bool = _SUBJECT_DEFAULT_THREAD_POOL_EXECUTOR_LOG
    ) -> None:
        """
        Create a new subject.

        There are three ways for a listener to listen to a subject:
        - Register a listener object (a sub-class of `Listener`) with the
          `field_changed()` method defined to the subject,
        - Register a (set of) callback(s) with the to the subject, or
        - Decorate method(s) of a class with `@call_on_field_change()` and
          register instances of that class with the subject.
        """
        self.__listeners = TwoWayMap[Listener, str]()
        self.__callbacks = TwoWayMap[Callable[..., None], str]()
        self.__executor = AloyThreadPool(
            pool_name="PubSubHub :: Thread Pool Executor",
            max_workers=max(max_workers, 1),
            thread_name_prefix="PubSubHub :: Thread Pool Executor :: Thread",
            profile=bool(profile),
            log=bool(log)
        )
        self.__queues: dict[str, deque[Any]] = defaultdict(deque)
        for field_name, (_, queue_size) \
                in self.__SUBJECT_FIELDS__.items():  # type: ignore
            if queue_size is not None:
                self.__queues[field_name] = deque(maxlen=queue_size)

    def __get_field__(self, field_name: str, new_value: bool = False) -> Any:
        get_attr_and_queue_size = \
            self.__SUBJECT_FIELDS__.get(field_name)  # type: ignore
        if get_attr_and_queue_size is None:
            raise AttributeError(
                f"Subject {self} has no field {field_name}."
            )
        get_attr, queue_size = get_attr_and_queue_size
        value = get_attr(self)
        if queue_size is not None:
            if new_value:
                self.__queues[field_name].append(value)
                return value
            else:
                return list(self.__queues[field_name])
        return value

    def __is_queued_field__(self, field_name: str) -> bool:
        return (
            self.__SUBJECT_FIELDS__.get(field_name)[1]  # type: ignore
            is not None
        )

    def __check_callback(self, callback: Callable[..., None]) -> None:
        """Check that the callback is a function that takes four arguments."""
        if not inspect.ismethod(callback) and not inspect.isfunction(callback):
            raise TypeError(
                f"Callback must be a method or function. Got; {callback}.")
        if len(inspect.signature(callback).parameters) != 4:
            raise TypeError(
                f"Callback must take four arguments. Got: {callback}.")

    @sync(lock="all")
    def register(
        self,
        listener_or_callback: (
            Listener
            | Callable[["Subject", str, Any, Any], None]
        ),
        *fields: str
    ) -> None:
        """
        Register a listener or callback with the subject. The listener or
        callback will be called when any of the given fields change.
        """
        if isinstance(listener_or_callback, Listener):
            listener = listener_or_callback
            if hasattr(listener, "field_changed"):
                self.__listeners.add_many(listener, fields)
            for attr_name in dir(listener):
                attr = getattr(listener, attr_name)
                if hasattr(attr, "__subject_field__"):
                    callback = attr
                    _field_name = callback.__subject_field__
                    try:
                        self.__check_callback(callback)
                    except TypeError as err:
                        raise TypeError(
                            f"Listener {listener} has an invalid callback."
                        ) from err
                    self.__callbacks.add(callback, _field_name)
        else:
            callback = listener_or_callback
            self.__check_callback(callback)
            self.__callbacks.add_many(callback, fields)

    @sync(lock="method", group_name="__update__")
    def update(self, *field_names: str) -> None:
        for field_name in field_names:
            current_value = self.__get_field__(field_name)
            self.__update__(field_name, None, current_value)

    def __update__(
        self,
        field_name: str,
        old_value: Any,
        new_value: Any
    ) -> None:
        self.__executor.submit(
            f"Subject Update ({field_name})",
            self.__update_async,
            field_name,
            old_value,
            new_value
        )

    def __update_async(
        self,
        field_name: str,
        old_value: Any,
        new_value: Any
    ) -> None:
        for listener in self.__listeners.backwards_get(field_name, []):
            try:
                value = listener.field_changed(
                    self, field_name, old_value, new_value)
                if value is NotImplemented:
                    with self.instance_lock:  # type: ignore
                        self.__listeners.remove(listener, field_name)
            except Exception as err:  # pylint: disable=broad-except
                self.__log_exception(
                    listener, field_name, old_value, new_value, err)
        for callback in self.__callbacks.backwards_get(field_name, []):
            try:
                callback(self, field_name, old_value, new_value)
            except Exception as err:  # pylint: disable=broad-except
                self.__log_exception(
                    callback, field_name, old_value, new_value, err)

    def __log_exception(
        self,
        listener_or_callback: Listener | Callable[..., None],
        field_name: str,
        old_value: Any,
        new_value: Any,
        exc_info: Exception | None
    ) -> None:
        name: str
        if isinstance(listener_or_callback, Listener):
            name = "Listener"
        else:
            name = "Callback"
        self.__SUBJECT_LOGGER.exception(
            "Subject %s: %s %s raised an exception, when "
            "updating field %s from %s to %s.",
            self, name, listener_or_callback, field_name, old_value, new_value,
            exc_info=exc_info
        )


def __main():
    """Entry point of the module."""
    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format="%(asctime)s %(levelname)s %(name)s %(message)s",
    #     stream=sys.stdout
    # )

    class MySubject(Subject):
        def __init__(self) -> None:
            super().__init__(log=True)
            self.__my_field = 0

        @property
        @field()
        def my_field(self) -> int:
            return self.__my_field

        @my_field.setter
        @field_change()
        def my_field(self, value: int) -> None:
            self.__my_field = value

    class MyListener(Listener):
        @call_on_field_change("my_field")
        def my_field_changed(
            self,
            source: Subject,
            field_name: str,
            old_value: int,
            new_value: int
        ) -> None:
            print(f"Listener {self} got notified that field {field_name} "
                  f"changed from {old_value} to {new_value}.")

    subject = MySubject()
    listener = MyListener()
    subject.register(listener)
    subject.my_field = 1
    subject.my_field = 1
    subject.my_field = 2
    subject.my_field = 2
    subject.my_field = 3
    subject.my_field = 3
    subject.my_field = 4
    subject.my_field = 4
    subject.my_field = 5
    subject.my_field = 5
    # time.sleep(1)


if __name__ == "__main__":
    __main()
