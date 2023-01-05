#!/usr/bin/env python3
""" 100-safe_first_element mod """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ returns the first element of a list or None """
    if lst:
        return lst[0]
    else:
        return None
