"""Unix Match. Part 2.

URL: https://py.checkio.org/en/mission/unix-match-part-2/
DESCRIPTION:
    You need to find out if the given unix pattern matches the given filename.
    Here is a small table that shows symbols that can be used in patterns.
    [seq]	matches any character in seq, for example [123] means any
    character - '1', '2' or '3'
    [!seq]	matches any character not in seq, for example [!123] means
    any character except '1', '2' and '3'
    []	seq without any chars will never match
    Note that the expression in one pair of square brackets responds
    only for 1 character. So
    ('0123', '[!abc]123') == True, but ('00123', '[!abc]123') = False
INPUT/OUTPUT EXAMPLE:
    unix_match('somefile.txt', 'somefile.txt') == True
    unix_match('1name.txt', '[!abc]name.txt') == True
    unix_match('log1.txt', 'log[1234567890].txt') == True
"""
import re


def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace('!', '^').replace('[^]', r'\[!]')
    try:
        return True if re.match(pattern, filename) else False
    except Exception:
        return False


def main():
    print(
        f"unix_match('somefile.txt', '*') == "
        f"{unix_match('somefile.txt', '*')}")


if __name__ == '__main__':
    main()
