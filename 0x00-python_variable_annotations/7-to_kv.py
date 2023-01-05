#!/usr/bin/env python3
"""
    7-to_kv mod
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple of string and float """
    return (k, v**2)
