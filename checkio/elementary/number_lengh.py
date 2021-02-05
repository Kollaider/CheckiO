"""Number Lengh.

URL: https://py.checkio.org/mission/number-length/solve/
DESCRIPTION:
    You have a positive integer. Try to find out how many digits it has?
INPUT/OUTPUT EXAMPLE:
    first_word("Hello world") == "Hello"
    first_word("a word") == "a"
    first_word("hi") == "hi"
"""


def number_length(a: int) -> int:
    return len(str(a))


def main():
    print('Example:')
    print(number_length(10))


if __name__ == '__main__':
    main()
