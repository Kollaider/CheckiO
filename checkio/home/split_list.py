"""Split list.

URL: https://py.checkio.org/en/mission/split-list/
DESCRIPTION:
    You have to split a given array into two arrays.
    If it has an odd amount of elements, then the first array should
    have more elements. If it has no elements, then two empty
    arrays should be returned.
INPUT/OUTPUT EXAMPLE:
    split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    split_list([1, 2, 3]) == [[1, 2], [3]]
    split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    split_list([1]) == [[1], []]
    split_list([]) == [[], []]
"""

import math


def split_list(items: list) -> list:
    ml = math.ceil(len(items) / 2)
    return [items[0:ml], items[ml:]]


def main():
    print(
        f'split_list([1, 2, 3, 4, 5, 6]) == '
        f'{split_list([1, 2, 3, 4, 5, 6])}')


if __name__ == '__main__':
    main()
