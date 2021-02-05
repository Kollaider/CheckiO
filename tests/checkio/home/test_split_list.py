from unittest import TestCase

from checkio.home.split_list import split_list


class SplitListTestCase(TestCase):

    def test__even_list__valid_result(self):
        input_data = [1, 2, 3, 4, 5, 6]
        actual_result = split_list(input_data)
        expected_result = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(expected_result, actual_result)

    def test__odd_list__valid_result(self):
        input_data = [1, 2, 3, 4, 5]
        actual_result = split_list(input_data)
        expected_result = [[1, 2, 3], [4, 5]]
        self.assertEqual(expected_result, actual_result)
