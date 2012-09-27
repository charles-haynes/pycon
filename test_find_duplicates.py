import find_duplicates
from mock import call, Mock, patch

__author__ = 'chaynes'

import unittest

@patch('os.path.join', Mock(side_effect=(lambda x, y: x + '/' + y)))
class MyTestCase(unittest.TestCase):
    def setUp(self):
        walk_return = [('root_dir', ['a', ], ['b', ]), ('root_dir/a', [], ['c', 'd']), ]

        walk_patcher = patch('os.walk', Mock(return_value=walk_return))
        walk_patcher.start()
        self.addCleanup(walk_patcher.stop)

    def test_find_duplicates_recursively_adds_all_files_in_dir(self):
        with patch('file_store.FileStore.Add') as mock_add:
            find_duplicates.main('root_dir')

            expected = [call('root_dir/b'), call('root_dir/a/c'), call('root_dir/a/d')]
            self.assertEqual(expected, mock_add.call_args_list)

    @patch('file_store.FileStore.Hash', Mock(return_value=12345))
    def test_find_duplicates_deletes_duplicates(self):
        with patch('os.unlink') as mock_unlink:
            find_duplicates.main('root_dir')

            expected = [call('root_dir/a/c'), call('root_dir/a/d')]
            self.assertEqual(expected, mock_unlink.call_args_list)

    if __name__ == '__main__':
        unittest.main()
