"""Sum Numbers.

URL: https://py.checkio.org/en/mission/sum-numbers/
DESCRIPTION:
    In a given text you need to sum the numbers. Only separated numbers should
    be counted. If a number is part of a word it shouldn't be counted.
    The text consists from numbers, spaces and english letters
INPUT/OUTPUT EXAMPLE:
    sum_numbers('hi') == 0
    sum_numbers('who is 1st here') == 0
    sum_numbers('my numbers is 2') == 2
"""


def sum_numbers(text: str) -> int:
    text = text.split()
    return sum(int(num) for num in text if num.isdigit())


def main():
    print(f"sum_numbers('hi') == {sum_numbers('hi')}")


if __name__ == '__main__':
    main()
