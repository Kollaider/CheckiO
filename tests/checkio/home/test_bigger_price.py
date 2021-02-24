from unittest import TestCase

from checkio.home.bigger_price import bigger_price


class SplitListTestCase(TestCase):

    def test__bigger_price__equal_result(self):
        input_data = (2, [
            {'name': 'bread', 'price': 100},
            {'name': 'wine', 'price': 138},
            {'name': 'meat', 'price': 15},
            {'name': 'water', 'price': 1},
        ])
        actual_result = bigger_price(*input_data)
        expected_result = [
            {'name': 'wine', 'price': 138},
            {'name': 'bread', 'price': 100}]
        self.assertEqual(expected_result, actual_result)

        input_data_2 = (1, [
            {'name': 'pen', 'price': 5},
            {'name': 'whiteboard', 'price': 170},
        ])
        actual_result_2 = bigger_price(*input_data_2)
        expected_result_2 = [{'name': 'whiteboard', 'price': 170}]
        self.assertEqual(expected_result_2, actual_result_2)
