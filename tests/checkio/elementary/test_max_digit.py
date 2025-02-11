from unittest import TestCase

from checkio.elementary.max_digit import max_digit


class MaxDigitsTestCase(TestCase):

    def test__max_digit__equal_value(self):
        self.assertEqual(0, max_digit(0))
        self.assertEqual(5, max_digit(52))
        self.assertEqual(6, max_digit(634))
        self.assertEqual(1, max_digit(10000))
