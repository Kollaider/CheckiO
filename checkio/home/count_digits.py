"""Count Digits.

URL: https://py.checkio.org/en/mission/count-digits/
DESCRIPTION:
    You need to count the number of digits in a given string.
INPUT/OUTPUT EXAMPLE:
    count_digits('hi') == 0
    count_digits('who is 1st here') == 1
    count_digits('my numbers is 2') == 1
    count_digits('This picture is an oil on canvas '
        'painting by Danish artist Anna '
        'Petersen between 1845 and 1910 year') == 8
    count_digits('5 plus 6 is') == 2
    count_digits('') == 0
"""


def count_digits(text: str) -> int:
    return len(list(filter(lambda ch: ch.isdigit(), text)))


def main():
    print(f"count_digits('hi') == {count_digits('hi')}")


if __name__ == '__main__':
    main()
