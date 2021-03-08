from unittest import TestCase

from checkio.electronic_station.unix_match_part_1 import unix_match


class UnixMaxPartOneTestCase(TestCase):

    def test__unix_max_part_one__valid_result(self):
        self.assertEqual(True, unix_match('somefile.txt', '*'))
        self.assertEqual(True, unix_match('other.exe', '*'))
        self.assertEqual(False, unix_match('my.exe', '*.txt'))
        self.assertEqual(True, unix_match('log1.txt', 'log?.txt'))
        self.assertEqual(False, unix_match('log12.txt', 'log?.txt'))
        self.assertEqual(True, unix_match('log12.txt', 'log??.txt'))
