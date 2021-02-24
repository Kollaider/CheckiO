"""Days Between.

URL: https://py.checkio.org/en/mission/days-diff/
DESCRIPTION:
    You are given two dates as an array with three numbers - a year,
     month and day. For example: 19 April 1982 will be (1982, 4, 19).
     You should find the difference in days between the given dates.
     For example between today and tomorrow = 1 day.
     The difference will always be either a positive number or zero,
     so don't forget about the absolute value.
INPUT/OUTPUT EXAMPLE:
    days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    days_diff((2014, 1, 1), (2014, 8, 27)) == 238
"""


import datetime


def days_diff(a: tuple, b: tuple) -> int:
    date1 = datetime.date(a[0], a[1], a[2])
    date2 = datetime.date(b[0], b[1], b[2])
    date = date2 - date1
    return abs(date.days)


def main():
    print(f'days_diff((1982, 4, 19), (1982, 4, 22)) == '
          f'{days_diff((1982, 4, 19), (1982, 4, 22))}')


if __name__ == '__main__':
    main()
