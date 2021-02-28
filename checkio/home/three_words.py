"""Three Words.

URL: https://py.checkio.org/en/mission/three-words/
DESCRIPTION:
    You are given a string with words and numbers separated
    by whitespaces (one space).
    The words contains only letters. You should check
    if the string contains three words in succession.
    For example, the string "start 5 one two three 7 end"
    contains three words in succession.
INPUT/OUTPUT EXAMPLE:
    checkio("Hello World hello") == True
    checkio("He is 123 man") == False
    checkio("1 2 3 4") == False
    checkio("bla bla bla bla") == True
    checkio("Hi") == False
"""


def checkio(words: str) -> bool:
    words = words.split()
    count = 0
    for word in words:
        if word.isalpha():
            count += 1
        else:
            count = 0
    return count > 2


def main():
    print(checkio('Hello World hello'))


if __name__ == '__main__':
    main()
