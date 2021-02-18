from unittest import TestCase

from checkio.elementary.first_word import first_word


class FirstWordTestCase(TestCase):

    def test__first_word__valid_result(self):
        self.assertEqual('Hello', first_word('Hello world'))
        self.assertEqual('a', first_word('a word'))
        self.assertEqual('hi', first_word('hi'))
        self.assertEqual('New', first_word('New Year'))
