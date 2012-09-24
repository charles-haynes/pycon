import file_dictionary
from mock import Mock, patch

TEST_FILE_NAME = 'test_file_name'
TEST_FILE_NAME2 = 'test_file_name_2'
TEST_DIGEST = 12345

__author__ = 'chaynes'

import unittest

@patch('io.open', Mock())
class FileDictionaryTests(unittest.TestCase):
    def setUp(self):
        self.file_dictionary = file_dictionary.FileDictionary()

    @patch('hashlib.md5')
    def test_can_add_file(self, mock_digest):
        self.file_dictionary.Add(TEST_FILE_NAME)

        self.assertTrue(mock_digest.called)

    @patch('hashlib.md5', Mock())
    def test_adding_duplicate_key_raises_error(self):
        self.file_dictionary.Add(TEST_FILE_NAME)

        with self.assertRaises(file_dictionary.DuplicateEntry):
            self.file_dictionary.Add(TEST_FILE_NAME)

    @patch('hashlib.md5', Mock(return_value=TEST_DIGEST))
    def test_adding_duplicate_digest_creates_duplicate_value(self):
        self.file_dictionary.Add(TEST_FILE_NAME)
        self.file_dictionary.Add(TEST_FILE_NAME2)

        test_dict = {TEST_FILE_NAME: TEST_DIGEST, TEST_FILE_NAME2: TEST_DIGEST}
        self.assertDictEqual(test_dict, self.file_dictionary.Dict())

if __name__ == '__main__':
    unittest.main()
