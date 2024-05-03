"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""
from typing import List


def solution(args: List[int]) -> str:
    result = []
    i = 0
    while i < len(args):
        start = args[i]
        end = start
        while i + 1 < len(args) and args[i + 1] == end + 1:
            end = args[i + 1]
            i += 1
        if end == start:
            result.append(str(start))
        elif end == start + 1:
            result.extend([str(start), str(end)])
        else:
            result.append(f"{start}-{end}")
        i += 1
    return ",".join(result)


assert solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19,
                 20]) == "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
