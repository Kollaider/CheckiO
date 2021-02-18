"""Number Lengh.

URL: https://py.checkio.org/mission/number-length/solve/
DESCRIPTION:
    You have a positive integer. Try to find out how many digits it has?
INPUT/OUTPUT EXAMPLE:
    number_length(10) == 2
    number_length(0) == 1
"""


def number_length(a: int) -> int:
    return len(str(a))


def main():
    print(f'number_length(10) == {number_length(10)}')


if __name__ == '__main__':
    main()
