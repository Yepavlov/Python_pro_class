"""
Task
Given a string s of lowercase letters ('a' - 'z'), get the maximum distance between two same letters, and return
this distance along with the letter that formed it.

If there is more than one letter with the same maximum distance, return the one that appears in s first.

Input/Output
[input] string s
A string of lowercase Latin letters, where at least one letter appears twice.

[output] a string
The letter that formed the maximum distance and the distance itself.

Example
For s = "fffffahhhhhhaaahhhhbhhahhhhabxx", the output should be "a23".

The maximum distance is formed by the character 'a' from index 5 to index 27 (0-based). Therefore, the answer is "a23".
"""


def dist_same_letter(st: str) -> str:
    max_distance = 0
    max_letter = ""
    letter_position = {}

    for i, letter in enumerate(st):
        if letter in letter_position:
            distance = i - letter_position[letter]
            if distance > max_distance:
                max_distance = distance
                max_letter = letter
        else:
            letter_position[letter] = i

    return max_letter + str(max_distance + 1)


assert dist_same_letter("fffffahhhhhhaaahhhhbhhahhhhabxx") == "a23"
assert dist_same_letter("ucabcabcabcdfxhuizfgrsuixacbcx") == "c28"
assert dist_same_letter("iaufzhaifxhuzofghabcbacdbuzoxih") == "i30"
assert dist_same_letter("axaxfaaiiiofizxuiox") == "x18"
assert dist_same_letter("fxfaufhacaaacaaabbbabaddb") == "a19"
assert dist_same_letter("haaafhahhhuuuiuuuuiiifxxx") == "f18"
assert dist_same_letter("fxauf") == "f5"
