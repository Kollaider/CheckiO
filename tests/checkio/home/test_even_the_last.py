from unittest import TestCase

from checkio.home.even_the_last import checkio


class EvenTheLastTestCase(TestCase):

    def test__even_the_last__equal_value(self):
        self.assertEqual(30, checkio([0, 1, 2, 3, 4, 5]))
        self.assertEqual(30, checkio([1, 3, 5]))
        self.assertEqual(36, checkio([6]))
        self.assertEqual(0, checkio([]))
