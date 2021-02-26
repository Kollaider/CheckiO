from unittest import TestCase

from checkio.elementary.nearest_value import nearest_value


class NearestValueTestCase(TestCase):

    def test__nearest_oreder__valid_result(self):
        self.assertEqual(10, nearest_value({4, 7, 10, 11, 12, 17}, 9))
        self.assertEqual(7, nearest_value({4, 7, 10, 11, 12, 17}, 8))
        self.assertEqual(8, nearest_value({4, 8, 10, 11, 12, 17}, 9))
        self.assertEqual(9, nearest_value({4, 9, 10, 11, 12, 17}, 9))
        self.assertEqual(4, nearest_value({4, 7, 10, 11, 12, 17}, 0))
        self.assertEqual(17, nearest_value({4, 7, 10, 11, 12, 17}, 100))
        self.assertEqual(8, nearest_value({5, 10, 8, 12, 89, 100}, 7))
        self.assertEqual(-1, nearest_value({-1, 2, 3}, 0))
