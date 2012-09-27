__author__ = 'chaynes'

import unittest
import file_enumerator
from mock import Mock, patch

walk_return = [('root_dir', ['a', ], ['b', ]), ('root_dir/a', [], ['c', 'd']), ]

class FileEnumeratorTests(unittest.TestCase):
    @patch('os.path.join', Mock(side_effect=(lambda x, y: x + '/' + y)))
    @patch('os.walk', Mock(return_value=walk_return))
    def test_file_enumerator_recursively_lists_all_files_in_dir(self):
        files = [x for x in file_enumerator.files('root_dir')]

        expected = ['root_dir/b', 'root_dir/a/c', 'root_dir/a/d']
        self.assertEqual(expected, files)

if __name__ == '__main__':
    unittest.main()
