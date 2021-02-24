from unittest import TestCase

from checkio.electronic_station.words_order import words_order


class WordsOrderTestCase(TestCase):

    def test__words_order__valid_result(self):
        self.assertEqual(
            True,
            words_order('hi world im here', ['world', 'here']))
        self.assertEqual(
            False,
            words_order('hi world im here', ['here', 'world']))
        self.assertEqual(
            True,
            words_order('hi world im here', ['world']))
        self.assertEqual(
            False,
            words_order('hi world im here', ['world', 'here', 'hi']))
        self.assertEqual(
            True,
            words_order('hi world im here', ['world', 'im', 'here']))
        self.assertEqual(
            False, words_order('hi world im here', ['world', 'hi', 'here']))
        self.assertEqual(
            False, words_order('hi world im here', ['world', 'world']))
        self.assertEqual(
            False, words_order('hi world im here', ['country', 'world']))
        self.assertEqual(
            False, words_order('hi world im here', ['wo', 'rld']))
        self.assertEqual(
            False, words_order('', ['world', 'here']))
