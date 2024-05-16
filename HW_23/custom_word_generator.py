from faker import Faker


def custom_word_generator(num: int) -> str:
    if num > 10_000:
        raise ValueError("The number of words should not exceed 10 000.")
    faker = Faker()
    used_words = set()
    while len(used_words) < num:
        word = faker.word()
        if word not in used_words:
            used_words.add(word)
            yield word


generator = custom_word_generator(100)

for word in generator:
    print(word)
