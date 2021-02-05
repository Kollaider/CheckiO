from unittest import TestCase

from checkio.elementary.correct_sentence import correct_sentence


class CorrectSentenceTestCase(TestCase):

    def test__correct_sentence__valid_result(self):
        self.assertEqual('Greetings, friends.',
                         correct_sentence('greetings, friends'))
        self.assertEqual('Greetings, friends.',
                         correct_sentence('Greetings, friends'))
        self.assertEqual('Greetings, friends.',
                         correct_sentence('greetings, friends'))
        self.assertEqual('Hi.',
                         correct_sentence('Hi'))
        self.assertEqual('Welcome to New York.',
                         correct_sentence('welcome to New York'))
