"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(s: str) -> dict:
    return {char: s.count(char) for char in s}


assert count("aba") == {'a': 2, 'b': 1}
assert count("") == {}
assert count("fCaaBbcc") == {'C': 1, 'c': 2, 'B': 1, 'b': 1, 'a': 2, 'f': 1}
