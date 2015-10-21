#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using for loops."""


def process_data(data):
    """
    Args:
        data(mixed): A list or tuple containing numbers

    Returns:
        tuple: Sum and average of data
    """

    datapoint = 0

    for item in data:
        datapoint += item
        average = datapoint / float(len(data))

    return (datapoint, average)
