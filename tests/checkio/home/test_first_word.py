from unittest import TestCase

from checkio.home.first_word import first_word


class FirstWordTestCase(TestCase):

    def test__first_word__equal_result(self):
        self.assertEqual('Hello', first_word('Hello world'))
        self.assertEqual('a', first_word(' a word'))
        self.assertEqual("don't", first_word("don't touch it"))
        self.assertEqual('greetings', first_word('greetings, friends'))
        self.assertEqual('and', first_word('... and so on ...'))
        self.assertEqual('hi', first_word('hi'))
