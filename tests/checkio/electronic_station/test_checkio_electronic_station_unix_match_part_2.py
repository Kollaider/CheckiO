from unittest import TestCase

from checkio.electronic_station.unix_match_part_2 import unix_match


class UnixMaxPartTwoTestCase(TestCase):

    def test__unix_max_part_one__valid_result(self):
        self.assertEqual(True, unix_match('somefile.txt', 'somefile.txt'))
        self.assertEqual(True, unix_match('1name.txt', '[!abc]name.txt'))
        self.assertEqual(True, unix_match('log1.txt', 'log[!0].txt'))
        self.assertEqual(True, unix_match('log1.txt', 'log[1234567890].txt'))
        self.assertEqual(False, unix_match('log1.txt', 'log[!1].txt'))
