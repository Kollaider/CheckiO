"""Backward string.

URL: https://py.checkio.org/en/mission/backward-string/
DESCRIPTION:
    You should return a given string in reverse order.
INPUT/OUTPUT EXAMPLE:
    backward_string('val') == 'lav'
    backward_string('') == ''
    backward_string('ohho') == 'ohho'
    backward_string('123456789') == '987654321'
"""


def backward_string(val: str) -> str:
    # your code here
    return val[::-1]


def main():
    print('Example:')
    print(backward_string('val'))


if __name__ == '__main__':
    main()
