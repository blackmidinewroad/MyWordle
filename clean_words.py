from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / 'game/static/text'


def clean_data(filename: str) -> list[str]:
    with open(DATA_DIR / filename, encoding='utf-8') as file:
        file.readline()
        out = file.readlines()

    out.pop()

    for i, word in enumerate(out):
        out[i] = word.strip(' "",\n') + '\n'

    return out


def load_words(filename: str) -> list[str]:
    with open(DATA_DIR / filename, encoding='utf-8') as file:
        out = file.readlines()

    return out


valid_words = load_words('answer_words.txt')
dictionary = load_words('dictionary.txt')


def save_answer_words(data: list[str], filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as out:
        out.writelines(data)


def save_dictionary(data: list[str], added_valid_words, filename: str) -> None:
    valid_words_set = set(added_valid_words)

    with open(filename, 'w', encoding='utf-8') as out:
        for word in data:
            if word not in valid_words_set:
                out.write(word)


save_answer_words(valid_words, 'answer_words.txt')
save_dictionary(dictionary, valid_words, 'dictionary.txt')
