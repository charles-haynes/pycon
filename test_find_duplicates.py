import find_duplicates
from mock import call, Mock, patch

__author__ = 'chaynes'

import unittest

walk_return = [('root_dir', ['a', ], ['b', ]), ('root_dir/a', [], ['c', 'd']), ]

class MyTestCase(unittest.TestCase):
    @ patch('os.walk', Mock(return_value=walk_return))
    @ patch('os.path.join', Mock(side_effect=(lambda x, y: x + '/' + y)))
    def test_find_duplicates_recursively_adds_all_files_in_dir(self):
        expected = [call('root_dir/b'), call('root_dir/a/c'), call('root_dir/a/d')]
        with patch('file_dictionary.FileDictionary.Add') as mock_add:
            find_duplicates.find_duplicates('root_dir')

            self.assertEqual(expected, mock_add.call_args_list)

if __name__ == '__main__':
    unittest.main()
