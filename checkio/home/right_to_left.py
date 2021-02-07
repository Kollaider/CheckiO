"""Right To Left.

URL: https://py.checkio.org/en/mission/right-to-left/
DESCRIPTION:
    You are given a sequence of strings. You should join these
    strings into a chunk of text where the initial strings are
    separated by commas. As a joke on the right handed robots,
    you should replace all cases of the words "right" with
    the word "left", even if it's a part of another word.
    All strings are given in lowercase.
INPUT/OUTPUT EXAMPLE:
    left_join(("left", "right", "left", "stop")) ==
                "left,left,left,stop", "All to left"
    left_join(("bright aright", "ok")) ==
                "bleft aleft,ok", "Bright Left"
    left_join(("brightness wright",)) ==
                "bleftness wleft", "One phrase"
    left_join(("enough", "jokes")) ==
                "enough,jokes", "Nothing to replace"
"""


def left_join(phrases: tuple) -> str:
    lst = []
    for phrase in phrases:
        lst.append(phrase.replace('right', 'left')) \
            if 'right' in phrase else (lst.append(phrase))
    return ','.join(lst)


def main():
    print('Example:')
    print(left_join(('left', 'right', 'left', 'stop')))


if __name__ == '__main__':
    main()
