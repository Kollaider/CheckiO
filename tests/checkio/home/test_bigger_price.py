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
            {'name': 'bread', 'price': 100},
        ]
        self.assertEqual(expected_result, actual_result)
