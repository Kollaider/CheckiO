from unittest import TestCase

from checkio.elementary.end_zeros import end_zeros


class EndZerosTestCase(TestCase):

    def test__end_zeros__valid_result(self):
        self.assertEqual(1, end_zeros(0))
        self.assertEqual(0, end_zeros(1))
        self.assertEqual(1, end_zeros(10))
        self.assertEqual(0, end_zeros(101))
        self.assertEqual(0, end_zeros(245))
        self.assertEqual(2, end_zeros(100100))
