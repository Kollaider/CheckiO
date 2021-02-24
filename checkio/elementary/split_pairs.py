"""Split pairs.

URL: https://py.checkio.org/en/mission/split-pairs/
DESCRIPTION:
    Split the string into pairs of two characters. If the string contains
    an odd number of characters, then the missing second character of
    the final pair should be replaced with an underscore ('_').
INPUT/OUTPUT EXAMPLE:
    list(split_pairs('abcd')) == ['ab', 'cd']
    list(split_pairs('abc')) == ['ab', 'c_']
    list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    list(split_pairs('a')) == ['a_']
    list(split_pairs('')) == []
"""


def split_pairs(text: str) -> list:
    return [ch1 + ch2 for ch1, ch2 in zip(text[::2], text[1::2] + '_')]


def main():
    print(f"split_pairs('abcd') == {split_pairs('abcd')}")


if __name__ == '__main__':
    main()
