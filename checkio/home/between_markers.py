"""Between markers.

URL: https://py.checkio.org/en/mission/between-markers/
DESCRIPTION:
    You are given a string and two markers (the initial and final).
    You have to find a substring enclosed between these two markers.
    But there are a few important conditions:
    The initial and final markers are always different.
        If there is no initial marker, then the first character
        should be considered the beginning of a string.
        If there is no final marker, then the last character
        should be considered the ending of a string.
        If the initial and final markers are missing then
        simply return the whole string.
        If the final marker comes before the initial marker,
        then return an empty string.
INPUT/OUTPUT EXAMPLE:
    between_markers('What is >apple<', '>', '<') == 'apple'
    between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
"""


def between_markers(text: str, begin: str, end: str) -> str:
    b, e = text.find(begin), text.find(end)

    if b == -1 and e == -1:
        return text

    if b == -1:
        return text[:e]
    if e == -1:
        return text[b + len(begin):]

    if b >= 0 and e >= 0:
        return text[b + len(begin):e]
    return ''


def main():
    print(
        f"between_markers('What is >apple<', '>', '<') == "
        f"{between_markers('What is >apple<', '>', '<')}")


if __name__ == '__main__':
    main()
