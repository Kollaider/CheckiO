"""Unix Match. Part 1.

URL: https://py.checkio.org/en/mission/unix-match-part-1/
DESCRIPTION:
    You need to find out if the given unix pattern matches the given filename.
    Let me show you what I mean by matching the filenames in the unix-shell.
    For example, * matches everything and *.txt matches all
    of the files that have txt extension. Here is a small table
    that shows symbols that can be used in patterns.
    *	matches everything
    ?	matches any single characte
INPUT/OUTPUT EXAMPLE:
    unix_match('somefile.txt', '*') == True
    unix_match('other.exe', '*') == True
    unix_match('my.exe', '*.txt') == False
    unix_match('log1.txt', 'log?.txt') == True
    unix_match('log12.txt', 'log?.txt') == False
    unix_match('log12.txt', 'log??.txt') == True
"""
import re


def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace('.', r'\.').replace('*', '.*').replace('?', '.')
    return bool(re.match(pattern, filename))


def main():
    print(unix_match('somefile.txt', '*'))


if __name__ == '__main__':
    main()
