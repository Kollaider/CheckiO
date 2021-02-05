from unittest import TestCase

from checkio.elementary.backward_string import backward_string


class EndZerosTestCase(TestCase):

    def test__backward_string__valid_result(self):
        self.assertEqual('lav', backward_string('val'))
        self.assertEqual('', backward_string(''))
        self.assertEqual('ohho', backward_string('ohho'))
        self.assertEqual('987654321', backward_string('123456789'))
