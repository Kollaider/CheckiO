"""End Zeros.

URL: https://py.checkio.org/en/mission/end-zeros/
DESCRIPTION:
    Try to find out how many zeros a given number has at the end.
INPUT/OUTPUT EXAMPLE:
    end_zeros(0) == 1
    end_zeros(1) == 0
    end_zeros(10) == 1
    end_zeros(101) == 0
"""
from itertools import takewhile


def end_zeros(number: int) -> int:
    return len(list(takewhile(lambda num: num == '0', str(number)[::-1])))


def main():
    print(end_zeros(0))


if __name__ == '__main__':
    main()
