"""Remove All Before.

URL: https://py.checkio.org/en/mission/remove-all-before/
DESCRIPTION:
    For the illustration we have a list [1, 2, 3, 4, 5] and we need to remove
    all elements that go before 3 - which is 1 and 2.
    We have two edge cases here:
    (1) if a cutting element cannot be found,
    then the list shoudn't be changed.
    (2) if the list is empty, then it should remain empty.
INPUT/OUTPUT EXAMPLE:
    list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]

    list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    list(remove_all_before([], 0)) == []
    list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))
     == [7, 7, 7, 7, 7, 7, 7, 7, 7]
"""


from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    try:
        ind = items.index(border)
        return items[ind:]
    except ValueError:
        return items


def main():
    print('Example:')
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))


if __name__ == '__main__':
    main()
