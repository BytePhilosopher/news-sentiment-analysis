import unittest
from src.data.loader import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_data_valid(self):
        # Test loading a valid dataset
        data = load_data('data/raw/sample_data.csv')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_load_data_invalid(self):
        # Test loading an invalid dataset
        with self.assertRaises(FileNotFoundError):
            load_data('data/raw/non_existent_file.csv')

if __name__ == '__main__':
    unittest.main()