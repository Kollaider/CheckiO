"""Acctptable Password I.

URL: https://py.checkio.org/mission/acceptable-password-i/solve/
DESCRIPTION:
    In this mission, you need to create a password verification function.
    The verification condition is:
    the length should be bigger than 6.
INPUT/OUTPUT EXAMPLE:
    is_acceptable_password('short') == False
    is_acceptable_password('muchlonger') == True
    is_acceptable_password('ashort') == False
"""


def is_acceptable_password(password: str) -> bool:
    return True if len(password) > 6 else False


def main():
    print(
        f"is_acceptable_password('short') == "
        f"{is_acceptable_password('short')}")


if __name__ == '__main__':
    main()
