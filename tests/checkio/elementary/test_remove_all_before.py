from unittest import TestCase

from checkio.elementary.remove_all_before import remove_all_before


class RemoveAllBeforeTestCase(TestCase):

    def test__remove_all_before__valid_result(self):
        self.assertEqual(
            [3, 4, 5],
            remove_all_before([1, 2, 3, 4, 5], 3))
        self.assertEqual(
            [2, 2, 3, 3],
            remove_all_before([1, 1, 2, 2, 3, 3], 2))
        self.assertEqual(
            [2, 4, 2, 3, 4],
            remove_all_before([1, 1, 2, 4, 2, 3, 4], 2))
        self.assertEqual(
            [],
            remove_all_before([], 0))
        self.assertEqual(
            [3, 4, 5],
            remove_all_before([1, 2, 3, 4, 5], 3))
        self.assertEqual(
            [7, 7, 7, 7, 7, 7, 7, 7, 7],
            remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))
