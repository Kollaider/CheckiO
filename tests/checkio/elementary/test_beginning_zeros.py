from unittest import TestCase

from checkio.elementary.beginning_zeros import beginning_zeros


class BeginningZerosTestCase(TestCase):

    def test__beginning_zeros__valid_result(self):
        self.assertEqual(0, beginning_zeros('100'))
        self.assertEqual(2, beginning_zeros('001'))
        self.assertEqual(0, beginning_zeros('100100'))
        self.assertEqual(2, beginning_zeros('001001'))
        self.assertEqual(4, beginning_zeros('0000'))
