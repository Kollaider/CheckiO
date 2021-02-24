"""Even The Last.

URL: https://py.checkio.org/en/mission/even-last/
DESCRIPTION:
    You are given an array of integers. You should find the sum
    of the integers with even indexes (0th, 2nd, 4th...).
    Then multiply this summed number and the final element
    of the array together. Don't forget that the first element
    has an index of 0.
    For an empty array, the result will always be 0 (zero).
INPUT/OUTPUT EXAMPLE:
    checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    checkio([6]) == 36, "(6)*6=36"
    checkio([]) == 0, "An empty array = 0"
"""


def checkio(array: list) -> int:
    return sum(array[::2]) * array[-1] if len(array) > 0 else 0


def main():
    print(f'checkio([0, 1, 2, 3, 4, 5]) == {checkio([0, 1, 2, 3, 4, 5])}')


if __name__ == '__main__':
    main()
