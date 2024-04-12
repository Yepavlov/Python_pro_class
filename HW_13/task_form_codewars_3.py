"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean
and be case-insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""


def xo(s: str) -> bool:
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    else:
        return False


assert xo("xoxo") is True
assert xo("xooxx") is False
assert xo("zpzpzpp") is True
assert xo("zzoo") is False

