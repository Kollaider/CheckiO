from unittest import TestCase

from checkio.home.popular_words import popular_words


class SplitListTestCase(TestCase):

    def test__popular_words__equal_result(self):
        self.assertEqual({'i': 4,
                          'was': 3,
                          'three': 0,
                          'near': 0,
                          }, popular_words('When I was One I had just begun When I was Two I was nearly new',
                                           ['i', 'was', 'three', 'near']))
