"""Between Markers.

URL: https://py.checkio.org/en/mission/between-markers-simplified/
DESCRIPTION:
    You are given a string and two markers (the initial one and final).
    You have to find a substring enclosed between these two markers.
    But there are a few important conditions.

    The initial and final markers are always different.
    The initial and final markers are always 1 char size.
    The initial and final markers always exist in a string and go one
    after another.
INPUT/OUTPUT EXAMPLE:
    between_markers('What is >apple<', '>', '<') == "apple"
    between_markers('What is [apple]', '[', ']') == "apple"
    between_markers('What is ><', '>', '<') == ""
    between_markers('>apple<', '>', '<') == "apple"
"""


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin) + 1:text.rfind(end)]


def main():
    print(
        f"between_markers('What is >apple<', '>', '<') == "
        f"{between_markers('What is >apple<', '>', '<')}")


if __name__ == '__main__':
    main()
