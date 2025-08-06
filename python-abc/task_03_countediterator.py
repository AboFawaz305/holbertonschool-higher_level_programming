#!/usr/bin/python3
"""
This module contains a counted iterator
"""


class CountedIterator:
    """
    this class represent a counted iterator
    """

    def __init__(self, data) -> None:
        """
        The constructor
        """
        self.count = 0
        self.data = iter(data)

    def get_count(self):
        """
        get the count
        """
        return self.count

    def __iter__(self):
        """
        return an iter
        """
        return self

    def __next__(self):
        """
        get next item
        """
        v = None
        try:
            v = next(self.data)
            self.count += 1
        except StopIteration as e:
            raise e
        return v


data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
