from unittest import TestCase

from checkio.elementary.between_markers import between_markers


class BetweenMarkersTestCase(TestCase):

    def test__between_markers__valid_result(self):
        self.assertEqual('apple', between_markers('What is >apple<', '>', '<'))
        self.assertEqual('apple', between_markers('What is [apple]', '[', ']'))
        self.assertEqual('', between_markers('What is ><', '>', '<'))
        self.assertEqual('apple', between_markers('>apple<', '>', '<'))
