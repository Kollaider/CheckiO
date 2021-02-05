"""Beginning Zeros.

URL: https://py.checkio.org/en/mission/beginning-zeros/
DESCRIPTION:
    You have a string that consist only of digits.
    You need to find how many zero digits ("0") are at
    the beginning of the given string.
INPUT/OUTPUT EXAMPLE:
    beginning_zeros('100') == 0
    beginning_zeros('001') == 2
    beginning_zeros('100100') == 0
    beginning_zeros('001001') == 2
"""


def beginning_zeros(number: str) -> int:
    num = 0
    for i in number:
        if i == '0':
            num += 1
        else:
            break
    return num


def main():
    print('Example:')
    print(beginning_zeros('100'))


if __name__ == '__main__':
    main()
