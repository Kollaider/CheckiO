from unittest import TestCase

from checkio.elementary.all_upper_1 import is_all_upper


class AllUpperTestCase(TestCase):

    def test__all_upper__valid_result(self):
        self.assertEqual(True, is_all_upper('ALL UPPER'))
        self.assertEqual(False, is_all_upper('all lower'))
        self.assertEqual(False, is_all_upper('mixed UPPER and lower'))
        self.assertEqual(True, is_all_upper(''))
