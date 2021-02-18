"""All Upper I.

URL: https://py.checkio.org/en/mission/all-upper/
DESCRIPTION:
    Check if a given string has all symbols in upper case.
    If the string is empty or doesn't have any letter
    in it - function should return True.
INPUT/OUTPUT EXAMPLE:
    is_all_upper('ALL UPPER') == True
    is_all_upper('all lower') == False
    is_all_upper('mixed UPPER and lower') == False
    is_all_upper('') == True
"""


def is_all_upper(text: str) -> bool:
    return all(text.isupper() for ch in text if ch.isalpha())


def main():
    print(f"is_all_upper('ALL UPPER') == {is_all_upper('ALL UPPER')}")


if __name__ == '__main__':
    main()
