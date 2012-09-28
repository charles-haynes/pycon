import main
from mock import call, Mock, patch

__author__ = 'chaynes'

import unittest

@patch('file_enumerator.files', Mock(return_value=['root_dir/b', 'root_dir/a/c', 'root_dir/a/d']))
class MainTest(unittest.TestCase):
    def test_find_duplicates_recursively_adds_all_files_in_dir(self):
        with patch('file_store.FileStore.Add') as mock_add:
            main.main('root_dir')

            expected = [call('root_dir/b'), call('root_dir/a/c'), call('root_dir/a/d')]
            self.assertEqual(expected, mock_add.call_args_list)

    @patch('file_store.FileStore.Hash', Mock(return_value=12345))
    def test_find_duplicates_deletes_duplicates(self):
        with patch('os.unlink') as mock_unlink:
            main.main('root_dir')

            expected = [call('root_dir/a/c'), call('root_dir/a/d')]
            self.assertEqual(expected, mock_unlink.call_args_list)

    if __name__ == '__main__':
        unittest.main()
