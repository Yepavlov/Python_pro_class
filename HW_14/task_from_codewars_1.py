"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text: str) -> str:
    text_list = text.replace("-", "_").split("_")
    result = text_list[0]
    for el in text_list[1::]:
        result += el.capitalize()
    return result


assert to_camel_case("the-stealth-warrior") == "theStealthWarrior"
assert to_camel_case("The_Stealth_Warrior") == "TheStealthWarrior"
assert to_camel_case("The_Stealth-Warrior") == "TheStealthWarrior"
