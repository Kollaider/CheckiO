"""Words Order.

URL: https://py.checkio.org/en/mission/words-order/
DESCRIPTION:
    You have a text and a list of words. You need to check if the
    words in a list appear in the same order as in the given text.

    Cases you should expect while solving this challenge:
    a word from the list is not in the text -
    your function should return False;
    any word can appear more than once in a text -
    use only the first one;
    two words in the given list are the same -
    your function should return False;
    the condition is case sensitive, which means 'hi' and 'Hi'
    are two different words;
    the text includes only English letters and spaces.
INPUT/OUTPUT EXAMPLE:
    words_order('hi world im here', ['world', 'here']) == True
    words_order('hi world im here', ['here', 'world']) == False
    words_order('hi world im here', ['world']) == True
    words_order('hi world im here',
"""


def words_order(text: str, words: list) -> bool:
    tx = text.split()
    if len(words) != len(set(words)):
        return False
    for word in words:
        if word not in tx:
            return False
        else:
            tx = tx[tx.index(word):]
    return True


def main():
    print('Example:')
    print(words_order('hi world im here', ['world', 'im', 'here']))


if __name__ == '__main__':
    main()
