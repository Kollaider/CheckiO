from unittest import TestCase

from checkio.home.days_between import days_diff


class DaysBetweenTestCase(TestCase):

    def test__days_between__equal_result(self):
        self.assertEqual(3, days_diff((1982, 4, 19), (1982, 4, 22)))
        self.assertEqual(238, days_diff((2014, 1, 1), (2014, 8, 27)))
        self.assertEqual(238, days_diff((2014, 8, 27), (2014, 1, 1)))
