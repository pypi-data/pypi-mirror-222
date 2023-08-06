# -*- coding: utf-8 -*-

from __future__ import annotations

__all__ = (
    "replace_if_none",
    "factory_if_none",
    "unwrap_or_default",
    "unwrap_or_factory",
)

from typing import TYPE_CHECKING, overload

if TYPE_CHECKING:
    from collections.abc import Callable

    from kaparoo.utils.types import T, U


@overload
def replace_if_none(optional: None, surrogate: U) -> U:
    ...


@overload
def replace_if_none(optional: T, surrogate: U) -> T:
    ...


def replace_if_none(optional: T | None, surrogate: U) -> T | U:
    """Replace the value if it is None.

    Args:
        optional: The optional value to be checked.
        surrogate: The value to be returned if `optional` is None.

    Returns:
        The `optional` value if it is not None, otherwise the `surrogate` value.
    """
    return surrogate if optional is None else optional


@overload
def factory_if_none(optional: None, factory: Callable[[], U]) -> U:
    ...


@overload
def factory_if_none(optional: T, factory: Callable[[], U]) -> T:
    ...


def factory_if_none(optional: T | None, factory: Callable[[], U]) -> T | U:
    """Replace the value using the factory if it is None.

    Args:
        optional: The optional value to be checked.
        factory: A callable that creates a value if `optional` is None.

    Returns:
        The `optional` value if it is not None, otherwise the value created by `factory`.
    """  # noqa: E501
    return factory() if optional is None else optional


def unwrap_or_default(
    optional: T | None,
    default: T,
    callback: Callable[[T], T] | None = None,
) -> T:
    """Unwrap the optional value or replace it with a default if it is None.

    Args:
        optional: The optional value to be checked.
        default: The value to be returned if `optional` is None.
        callback: An optional callable to be applied to the result. Defaults to None.

    Returns:
        The `optional` value if it is not None, otherwise the `default` value.
            If a `callback` is provided, it is applied to the result before returning.
    """
    result = replace_if_none(optional, default)
    return callback(result) if callable(callback) else result


def unwrap_or_factory(
    optional: T | None,
    factory: Callable[[], T],
    callback: Callable[[T], T] | None = None,
) -> T:
    """Unwrap the optional value or replace it using the factory if it is None.

    Args:
        optional: The optional value to be checked.
        factory: A callable that creates a value if `optional` is None.
        callback: An optional callable to be applied to the result. Defaults to None.

    Returns:
        The `optional` value if it is not None, otherwise the value created by `factory`.
            If `callback` is provided, it is applied to the result before returning.
    """  # noqa: E501
    result = factory_if_none(optional, factory)
    return callback(result) if callable(callback) else result
