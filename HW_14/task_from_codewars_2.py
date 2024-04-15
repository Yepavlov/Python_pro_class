"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s: str) -> str | bool:
    s_list = s.strip().split()
    result = "#" + "".join(word.capitalize() for word in s_list)
    if len(result) > 140 or len(result) == 1:
        return False
    else:
        return result


assert generate_hashtag(" Hello there thanks for trying my Kata") == "#HelloThereThanksForTryingMyKata"
assert generate_hashtag("    Hello     World   ") == "#HelloWorld"
assert generate_hashtag("") is False
