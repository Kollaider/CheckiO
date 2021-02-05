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


def end_zeros(num: int) -> int:
    num = str(num)
    n = 0
    for i in num[::-1]:
        if i == '0':
            n += 1
        else:
            break
    return n


def main():
    print('Example:')
    print(end_zeros(0))


if __name__ == '__main__':
    main()
