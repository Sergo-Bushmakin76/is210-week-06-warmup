#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using for loops to manipulate tuples/lists."""


def flip_keys(to_flip):
    """
    Args:
        to_flip (list): nested sequence.
        
    Returns:
        to_flip (list): reversed list.

    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """

    indx = 0

    for item in to_flip:
        to_flip[indx] = item[::-1]
        indx += 1
    return to_flip
