"""Replace First.

URL: https://py.checkio.org/en/mission/replace-first/
DESCRIPTION:
    In a given list the first element should become the last one.
    An empty list or list with only one element should stay the same.
INPUT/OUTPUT EXAMPLE:
    list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    list(replace_first([1])) == [1]
    list(replace_first([])) == []
"""

from typing import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        items.append(items.pop(0))
    return items


def main():
    print(f'replace_first([1, 2, 3, 4]) == {replace_first([1, 2, 3, 4])}')


if __name__ == '__main__':
    main()
