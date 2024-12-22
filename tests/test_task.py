import unittest
from unittest.mock import patch, MagicMock
from task import (
    parse_numbers,
    parse_strings,
    find_max,
    find_min,
    calculate_sum,
    count_symbols,
    count_words,
)


class TestTaskFunctions(unittest.TestCase):

    def test_parse_numbers(self):
        with patch('builtins.input', return_value="1,2,3,4,5"):
            result = parse_numbers()
            self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_parse_strings(self):
        with patch('builtins.input', return_value="hello world python test"):
            result = parse_strings()
            self.assertEqual(result, ["hello", "world", "python", "test"])

    def test_find_max(self):
        numbers = [1, 2, 3, 4, 5]
        result = find_max(numbers)
        self.assertEqual(result, 5)

    def test_find_min(self):
        numbers = [1, 2, 3, 4, 5]
        result = find_min(numbers)
        self.assertEqual(result, 1)

    def test_calculate_sum(self):
        numbers = [1, 2, 3, 4, 5]
        result = calculate_sum(numbers)
        self.assertEqual(result, 15)

    def test_count_symbols(self):
        words = ["hello", "world"]
        with patch('builtins.print') as mocked_print:
            count_symbols(words)
            mocked_print.assert_any_call("h: 1")
            mocked_print.assert_any_call("e: 1")
            mocked_print.assert_any_call("l: 3")
            mocked_print.assert_any_call("o: 2")
            mocked_print.assert_any_call("w: 1")
            mocked_print.assert_any_call("r: 1")
            mocked_print.assert_any_call("d: 1")

    def test_count_words(self):
        words = ["hello", "world", "hello"]
        with patch('builtins.print') as mocked_print:
            count_words(words)
            mocked_print.assert_any_call("hello: 2")
            mocked_print.assert_any_call("world: 1")


if __name__ == "__main__":
    unittest.main()
