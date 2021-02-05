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


def split_pairs(a):
    lst = []
    if len(a) == 0:
        return lst
    for i in range(len(a)):
        if i % 2 != 0 and i != 0:
            lst.append(a[i - 1] + a[i])
    else:
        if len(a) % 2 != 0:
            lst.append(a[i] + '_')
    return lst


def main():
    print('Example:')
    print(list(split_pairs('abcd')))


if __name__ == '__main__':
    main()
