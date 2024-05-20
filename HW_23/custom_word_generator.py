import random

import nltk
from nltk.corpus import words

nltk.download('words')


def custom_word_generator(num: int) -> str:
    if num > 10_000:
        raise ValueError("The number of words should not exceed 10 000.")
    word_list = list(
        set(words.words()))  # Remove duplicate words from the sequence to make sure that function
    # random.sample() return only unique words.
    if num > len(word_list):
        raise ValueError("Requested number of words exceeds available unique words.")
    selected_words = random.sample(word_list, num)
    for word in selected_words:
        yield word


generator = custom_word_generator(10000)

result_list = []
for word in generator:
    result_list.append(word)

print(result_list)
assert len(result_list) == len(set(result_list))
