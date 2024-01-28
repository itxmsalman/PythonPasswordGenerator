import unittest
from unittest.mock import patch
from python_password_generator import get_valid_input, ordinary_pass, mixed_pass

class TestPasswordGenerator(unittest.TestCase):

    @patch('builtins.input', side_effect=['8'])
    def test_get_valid_input_positive(self, mock_input):
        result = get_valid_input("Kindly enter a positive figure: ")
        self.assertEqual(result, 8)

    @patch('builtins.input', side_effect=['-3', '5'])
    def test_get_valid_input_retry(self, mock_input):
        result = get_valid_input("Kindly enter a positive figure: ")
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['abc', '9'])
    def test_get_valid_input_invalid_input(self, mock_input):
        result = get_valid_input("Kindly enter a positive figure: ")
        self.assertEqual(result, 9)

    @patch('builtins.print')
    def test_normal_pass(self, mock_print):
        # Assuming nr_letters, nr_symbols, and nr_numbers are set appropriately
        ordinary_pass()
        mock_print.assert_called_once()

    @patch('builtins.print')
    def test_hashed_pass(self, mock_print):
        # Assuming nr_letters, nr_symbols, and nr_numbers are set appropriately
        mixed_pass()
        mock_print.assert_called_once()

if __name__ == '__main__':
    unittest.main()
