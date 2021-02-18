"""Correct Sentence.

URL: https://py.checkio.org/en/mission/correct-sentence/
DESCRIPTION:
    For the input of your function, you will be given one sentence.
    You have to return a corrected version,
    that starts with a capital letter and ends with a period (dot).

    Pay attention to the fact that not all of the fixes are necessary.
    If a sentence already ends with a period (dot),
    then adding another one will be a mistake.
INPUT/OUTPUT EXAMPLE:
    correct_sentence("greetings, friends") == "Greetings, friends."
    correct_sentence("Greetings, friends") == "Greetings, friends."
    correct_sentence("Greetings, friends.") == "Greetings, friends."
"""


def correct_sentence(text: str) -> str:
    if not text.endswith('.'):
        text = text[0].upper() + text[1:] + '.'
    else:
        text[0].upper() + text[1:]

    return text


def main():
    print(
        f"correct_sentence('greetings, friends') == "
        f"{correct_sentence('greetings, friends')}")


if __name__ == '__main__':
    main()
