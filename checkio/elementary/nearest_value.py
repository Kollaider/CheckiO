"""Nearest Value.

URL: https://py.checkio.org/en/mission/nearest-value/
DESCRIPTION:
    Find the nearest value to the given one.
    You are given a list of values as set form and a value
    for which you need to find the nearest one.
    For example, we have the following set of numbers:
    4, 7, 10, 11, 12, 17, and we need to find the nearest
    value to the number 9. If we sort this set in the ascending order,
    then to the left of number 9 will be number 7 and to the right -
    will be number 10. But 10 is closer than 7,
    which means that the correct answer is 10.
    A few clarifications:
    If 2 numbers are at the same distance, you need to choose the smallest one;
    The set of numbers is always non-empty, i.e. the size is >=1;
    The given value can be in this set, which means that it’s the answer;
    The set can contain both positive and negative numbers,
    but they are always integers;
    The set isn’t sorted and consists of unique numbers.
INPUT/OUTPUT EXAMPLE:
    nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
"""
from typing import Set


def nearest_value(values: Set[int], one: int) -> int:
    ans = one
    mn = max(values)
    for number in sorted(values):
        if (number - one) < mn:
            ans = number
        mn = abs(number - one)
    return ans


def main():
    print(
        'nearest_value({4, 7, 10, 11, 12, 17}, 9)) == '
        f'{nearest_value({4, 7, 10, 11, 12, 17}, 9)}',
    )


if __name__ == '__main__':
    main()
