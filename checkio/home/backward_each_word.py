"""Backward Each Word.

URL: https://py.checkio.org/en/mission/backward-each-word/
DESCRIPTION:
    In a given string you should reverse every word, but the words
    should stay in their places.
INPUT/OUTPUT EXAMPLE:
    backward_string_by_word('') == ''
    backward_string_by_word('world') == 'dlrow'
    backward_string_by_word('hello world') == 'olleh dlrow'
    backward_string_by_word('hello   world') == 'olleh   dlrow'
"""


def backward_string_by_word(text: str) -> str:
    text2 = text.replace(' ', ' * ')
    words = text2.split()

    for i in range(len(words)):
        if words[i].isalpha():
            words[i] = words[i][::-1]

    words = ''.join(words).replace('*', ' ')

    return words


def main():
    print('Example:')
    print(backward_string_by_word(''))


if __name__ == '__main__':
    main()
