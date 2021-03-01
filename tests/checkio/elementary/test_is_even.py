from unittest import TestCase

from checkio.elementary.is_even import is_even


class IsEvenTestCase(TestCase):

    def test__is_even__equal_value(self):
        self.assertEqual(True, is_even(2))
        self.assertEqual(False, is_even(5))
        self.assertEqual(True, is_even(0))
