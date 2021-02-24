from unittest import TestCase

from checkio.elementary.split_pairs import split_pairs


class SplitPairsTestCase(TestCase):

    def test__split_pairs__valid_result(self):
        self.assertEqual(['ab', 'cd'], split_pairs('abcd'))
        self.assertEqual(['ab', 'c_'], split_pairs('abc'))
        self.assertEqual(['ab', 'cd', 'f_'], split_pairs('abcdf'))
        self.assertEqual([], split_pairs(''))
