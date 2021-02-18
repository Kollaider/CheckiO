"""First word.

URL: https://py.checkio.org/en/mission/first-word-simplified/
DESCRIPTION:
    You are given a string and you have to find its first word.
    The input string consists of only English letters and spaces.
    There aren’t any spaces at the beginning and the end of the string.
INPUT/OUTPUT EXAMPLE:
    first_word("Hello world") == "Hello"
    first_word("a word") == "a"
    first_word("hi") == "hi"
"""


def first_word(text: str) -> str:
    return text.split()[0]


def main():
    print(f"first_word('Hello world') == {first_word('Hello world')}")


if __name__ == '__main__':
    main()
