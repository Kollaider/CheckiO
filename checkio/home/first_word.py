"""First Word.

URL: https://py.checkio.org/en/mission/first-word/
DESCRIPTION:
    You are given a string where you have to find its first word.
    When solving a task pay attention to the following points:
        There can be dots and commas in a string.
        A string can start with a letter or, for example, a dot or space.
        A word can contain an apostrophe and it's a part of a word.
        The whole text can be represented with one word and that's it.
INPUT/OUTPUT EXAMPLE:
    first_word("Hello world") == "Hello"
    first_word("greetings, friends") == "greetings"
"""


import re


def first_word(text: str) -> str:
    pattern = r"[\w']+"
    return re.findall(pattern, text)[0]


def main():
    print('Example:')
    print(first_word('Hello world'))


if __name__ == '__main__':
    main()
