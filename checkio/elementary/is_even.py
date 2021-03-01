"""Is Even.

URL: https://py.checkio.org/en/mission/is-even/
DESCRIPTION:
    Check if the given number is even or not. Your function
    should return True if the number is even, and False if the
    number is odd.
INPUT/OUTPUT EXAMPLE:
    is_even(2) == True
    is_even(5) == False
    is_even(0) == True
"""


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


def main():
    print(f'is_even(2) == {is_even(2)}')


if __name__ == '__main__':
    main()
