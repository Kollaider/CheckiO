from unittest import TestCase

from checkio.home.three_words import checkio


class SplitListTestCase(TestCase):

    def test__three_words__equal_result(self):
        self.assertEqual(True, checkio('Hello World hello'))
        self.assertEqual(False, checkio('He is 123 man'))
        self.assertEqual(False, checkio('1 2 3 4'))
        self.assertEqual(True, checkio('bla bla bla bla'))
        self.assertEqual(False, checkio('Hi'))
