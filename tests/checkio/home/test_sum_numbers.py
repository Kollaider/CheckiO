from unittest import TestCase

from checkio.home.sum_numbers import sum_numbers


class SumNumbersTestCase(TestCase):

    def test__sum_numbers__equal_result(self):
        self.assertEqual(0, sum_numbers('hi'))
        self.assertEqual(0, sum_numbers('who is 1st here'))
        self.assertEqual(3755, sum_numbers('This picture is an oil on canvas '
                                           'painting by Danish artist Anna '
                                           'Petersen between 1845 '
                                           'and 1910 year'))
        self.assertEqual(11, sum_numbers('5 plus 6 is'))
        self.assertEqual(0, sum_numbers(''))
        self.assertEqual(0, sum_numbers('hi'))
