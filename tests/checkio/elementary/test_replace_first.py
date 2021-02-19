from unittest import TestCase

from checkio.elementary.replace_first import replace_first


class ReplaceFirstTestCase(TestCase):

    def test__replace_first__valid_result(self):
        self.assertEqual([2, 3, 4, 1], replace_first([1, 2, 3, 4]))
        self.assertEqual([1], replace_first([1]))
        self.assertEqual([], replace_first([]))
