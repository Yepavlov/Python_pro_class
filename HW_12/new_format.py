def new_format(string: str) -> str:
    string = str(string)
    result = ""
    while string:
        result = "." + string[-3:] + result
        string = string[:-3]
    return result.lstrip(".")


assert new_format("1000000") == "1.000.000"
assert new_format("100") == "100"
assert new_format("1000") == "1.000"
assert new_format("100000") == "100.000"
assert new_format("10000") == "10.000"
assert new_format("0") == "0"
