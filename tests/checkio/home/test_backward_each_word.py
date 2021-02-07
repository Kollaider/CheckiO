from unittest import TestCase

from checkio.home.backward_each_word import backward_string_by_word


class SplitListTestCase(TestCase):

    def test__beckward_each_word__equal_result(self):
        self.assertEqual('', backward_string_by_word(''))
        self.assertEqual('dlrow', backward_string_by_word('world'))
        self.assertEqual('olleh dlrow',
                         backward_string_by_word('hello world'))
        self.assertEqual('olleh   dlrow',
                         backward_string_by_word('hello   world'))
        self.assertEqual('emoclew ot a emag',
                         backward_string_by_word('welcome to a game'))
