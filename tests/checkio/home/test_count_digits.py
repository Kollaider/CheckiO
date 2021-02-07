from unittest import TestCase

from checkio.home.count_digits import count_digits


class SplitListTestCase(TestCase):

    def test__count_digits_equal_result(self):
        self.assertEqual(0, count_digits('hi'))
        self.assertEqual(1, count_digits('who is 1st here'))
        self.assertEqual(1, count_digits('my numbers is 2'))
        self.assertEqual(8, count_digits('This picture is an oil on canvas '
                                         'painting by Danish artist Anna '
                                         'Petersen between 1845 '
                                         'and 1910 year'))
        self.assertEqual(2, count_digits('5 plus 6 is'))
        self.assertEqual(0, count_digits(''))
