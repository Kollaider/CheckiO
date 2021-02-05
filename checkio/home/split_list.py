"""Split list.

URL: https://
DESCRIPTION:
    desc
INPUT/OUTPUT EXAMPLE:
    split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
"""

import math


def split_list(items: list) -> list:
    ml = math.ceil(len(items) / 2)
    return [items[0:ml], items[ml:]]


def main():
    print('Example:')
    print(split_list([1, 2, 3, 4, 5, 6]))


if __name__ == '__main__':
    main()
