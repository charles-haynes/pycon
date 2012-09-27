import canonical_name
from mock import  Mock, patch

__author__ = 'chaynes'

import unittest

@patch('os.path.join', Mock(side_effect=lambda *x: '/'.join(x)))
class CanonicalNameTest(unittest.TestCase):
    def setUp(self):
        self.dict = {'artist': 'test_artist',
                     'album': 'test_album',
                     'title': 'test_title'}
        patcher = patch('mutagen.easyid3.EasyID3', Mock(return_value=self.dict))
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_canonical_name_no_track_number(self):
        name = canonical_name.CanonicalName('test').name
        self.assertEqual('test_artist/test_album/test_title.mp3', name)

    def test_canonical_name_track_number(self):
        self.dict['tracknumber'] = '1'
        name = canonical_name.CanonicalName('test').name
        self.assertEqual('test_artist/test_album/01 - test_title.mp3', name)

    def test_canonical_name_compilation_no_track_number(self):
        self.dict['compilation'] = True
        name = canonical_name.CanonicalName('test').name
        self.assertEqual('Various Artists/test_album/test_artist - test_title.mp3', name)

    def test_canonical_name_compilation_track_number(self):
        self.dict['compilation'] = True
        self.dict['tracknumber'] = '02/10'
        name = canonical_name.CanonicalName('test').name
        self.assertEqual('Various Artists/test_album/02 - test_artist - test_title.mp3', name)

if __name__ == '__main__':
    unittest.main()
