#!/usr/bin/env python3
"""
    101-safely_get_value mod
"""
from typing import Mapping, Any, Union, TypeVar
# create generic type var
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ takes in a dict and returns an item from dict or default val """
    if key in dct:
        return dct[key]
    else:
        return default
