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
        self.file_dictionary = file_store.FileStore(self.hasher)

    def test_can_add_file(self):
        self.file_dictionary.Add(TEST_FILE_NAME)

        self.assertTrue(self.hasher.called)

    def test_adding_duplicate_key_raises_error(self):
        self.file_dictionary.Add(TEST_FILE_NAME)

        with self.assertRaises(file_store.DuplicateEntry):
            self.file_dictionary.Add(TEST_FILE_NAME2)

    def test_adding_duplicate_digest_creates_duplicate_value(self):
        self.file_dictionary.Add(TEST_FILE_NAME)
        self.hasher.return_value = TEST_DIGEST2
        self.file_dictionary.Add(TEST_FILE_NAME2)

        test_hashes = {TEST_DIGEST, TEST_DIGEST2}
        self.assertSetEqual(test_hashes, self.file_dictionary.Hashes())

if __name__ == '__main__':
    unittest.main()
