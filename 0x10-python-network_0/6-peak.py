#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(intlist):
    """Finds a peak in integer"""

    if not intlist:
        return None

    low, high = 0, len(intlist)

    while low < high:
        mid = (low + high) // 2

        if (mid == 0 or intlist[mid] >= intlist[mid - 1]) and \
           (mid == len(intlist) - 1 or intlist[mid] >= intlist[mid + 1]):
            return intlist[mid]

        if mid > 0 and intlist[mid] < intlist[mid + 1]:
            low = mid + 1
        elif mid > 0 and intlist[mid] < intlist[mid - 1]:
            high = mid
        else:
            return None

    return None
