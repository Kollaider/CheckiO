from unittest import TestCase

from checkio.home.right_to_left import left_join


class RightToLeftTestCase(TestCase):

    def test__right_to_left__equatl_rusult(self):
        self.assertEqual('left,left,left,stop', left_join(('left', 'right', 'left', 'stop')))
        self.assertEqual('bleft aleft,ok', left_join(('bright aright', 'ok')))
        self.assertEqual('enough,jokes', left_join(('enough', 'jokes')))
