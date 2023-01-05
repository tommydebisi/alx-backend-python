#!/usr/bin/env python3
""" 9-element_length mod """
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples """
    return [(i, len(i)) for i in lst]
