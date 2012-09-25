import file_store
from mock import Mock, patch

TEST_FILE_NAME = 'test_file_name'
TEST_FILE_NAME2 = 'test_file_name_2'
TEST_DIGEST = 12345
TEST_DIGEST2 = 123456

__author__ = 'chaynes'

import unittest

@patch('io.open', Mock())
class FileDictionaryTests(unittest.TestCase):
    def setUp(self):
        self.hasher = Mock(return_value=TEST_DIGEST)
        self.on_duplicate = Mock()
        self.file_dictionary = file_store.FileStore(self.on_duplicate, self.hasher)

    def test_can_add_file(self):
        self.file_dictionary.Add(TEST_FILE_NAME)

        self.assertEqual(1, self.hasher.call_count)

    def test_adding_duplicate_key_calls_on_duplicate(self):
        self.file_dictionary.Add(TEST_FILE_NAME)
        self.file_dictionary.Add(TEST_FILE_NAME2)

        self.on_duplicate.assert_called_once_with(TEST_FILE_NAME2)

    def test_adding_duplicate_digest_creates_duplicate_value(self):
        self.file_dictionary.Add(TEST_FILE_NAME)
        self.hasher.return_value = TEST_DIGEST2
        self.file_dictionary.Add(TEST_FILE_NAME2)

        test_hashes = {TEST_DIGEST, TEST_DIGEST2}
        self.assertSetEqual(test_hashes, self.file_dictionary.Hashes())

if __name__ == '__main__':
    unittest.main()
