"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""
num = 145263


def descending_order(num: int) -> int:
    num_str = str(num)
    result = int("".join((sorted(num_str, reverse=True))))
    return result


assert descending_order(145263) == 654321
assert descending_order(42145) == 54421

