from unittest import TestCase

from checkio.elementary.number_lengh import number_length


class NumberLenghTestCase(TestCase):

    def test__first_word__valid_result(self):
        self.assertEqual(2, number_length(10))
        self.assertEqual(1, number_length(0))
        self.assertEqual(1, number_length(4))
        self.assertEqual(2, number_length(44))
