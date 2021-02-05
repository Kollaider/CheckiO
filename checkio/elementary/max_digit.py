"""Max digit.

URL: https://py.checkio.org/en/mission/max-digit/
DESCRIPTION:
    You have a number and you need to determine which digit
    in this number is the biggest.
INPUT/OUTPUT EXAMPLE:
    max_digit(0) == 0
    max_digit(52) == 5
    max_digit(634) == 6
    max_digit(1) == 1
     max_digit(10000) == 1
"""


def max_digit(number: int) -> int:
    # your code here
    return int(max(str(number)))


def main():
    print('Example:')
    print(max_digit(0))


if __name__ == '__main__':
    main()
