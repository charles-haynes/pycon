import io
import mp3_file

__author__ = 'chaynes'

import unittest

ID3_HEADER = 'ID3\x00\x00\x00\x00\x00\x00\x01\x00'
ID3_TRAILER = 'TAG' + '\x00' * (128 - len('TAG'))

MP3_FILE_EMPTY = ''
MP3_FILE_TOO_SHORT = '12345'
MP3_FILE_NO_ID3 = '12345' + '\x00' * 200
MP3_FILE_ID3_HEADER = ID3_HEADER + MP3_FILE_NO_ID3
MP3_FILE_ID3_TRAILER = MP3_FILE_NO_ID3 + ID3_TRAILER
MP3_FILE_ID3_HEADER_AND_TRAILER = ID3_HEADER + MP3_FILE_NO_ID3 + ID3_TRAILER

class Mp3FileTest(unittest.TestCase):
    def test_data_empty(self):
        file = io.BytesIO(MP3_FILE_EMPTY)
        mp3 = mp3_file.Mp3File(file)
        self.assertEqual(MP3_FILE_EMPTY, mp3.data())

    def test_data_too_short(self):
        file = io.BytesIO(MP3_FILE_TOO_SHORT)
        mp3 = mp3_file.Mp3File(file)
        self.assertEqual(MP3_FILE_TOO_SHORT, mp3.data())

    def test_data_no_id3(self):
        file = io.BytesIO(MP3_FILE_NO_ID3)
        mp3 = mp3_file.Mp3File(file)
        self.assertEqual(MP3_FILE_NO_ID3, mp3.data())

    def test_data_id3_header(self):
        file = io.BytesIO(MP3_FILE_ID3_HEADER)
        mp3 = mp3_file.Mp3File(file)
        self.assertEqual(MP3_FILE_NO_ID3, mp3.data())

    def test_data_id3_trailer(self):
        file = io.BytesIO(MP3_FILE_ID3_TRAILER)
        mp3 = mp3_file.Mp3File(file)
        self.assertEqual(MP3_FILE_NO_ID3, mp3.data())

    def test_data_id3_header_and_trailer(self):
        file = io.BytesIO(MP3_FILE_ID3_HEADER_AND_TRAILER)
        mp3 = mp3_file.Mp3File(file)
        self.assertEqual(MP3_FILE_NO_ID3, mp3.data())

if __name__ == '__main__':
    unittest.main()
