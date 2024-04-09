"""
Create a function that filters a list with any data type and returns a list with int only."""
from collections import Counter
from typing import List


def filter_list(list_of_data: list) -> List[int]:
    """return a new list with the strings filtered out"""
    result = [el for el in list_of_data if isinstance(el, int)]
    return result


assert filter_list([1, 2, "3", "str"]) == [1, 2]
