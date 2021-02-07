from unittest import TestCase

from checkio.home.between_markers import between_markers


class SplitListTestCase(TestCase):

    def test__between_markets__equal_result(self):
        self.assertEqual('apple', between_markers('What is >apple<', '>', '<'))
        self.assertEqual('My new site',
                         between_markers('<head><title>My new site</title></head>',
                                         '<title>', '</title>'))
        self.assertEqual('No', between_markers('No[/b] hi', '[b]', '[/b]'))
        self.assertEqual('hi', between_markers('No [b]hi', '[b]', '[/b]'))
        self.assertEqual('No hi', between_markers('No hi', '[b]', '[/b]'))
        self.assertEqual('', between_markers('No <hi>', '>', '<'))
