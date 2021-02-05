from unittest import TestCase

from checkio.elementary.acceptable_password import is_acceptable_password


class AcceptablePasswordTestCase(TestCase):

    def test__first_word__valid_result(self):
        self.assertEqual(False, is_acceptable_password('short'))
        self.assertEqual(True, is_acceptable_password('muchlongoer'))
        self.assertEqual(False, is_acceptable_password('ashort'))
