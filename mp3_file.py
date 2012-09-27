import io
import struct
from mutagen.id3 import BitPaddedInt

__author__ = 'chaynes'

class Mp3File(object):
    def __init__(self, file):
        self.file = file
        self.start = 0
        self.end = self.file.seek(0, io.SEEK_END)
        self.start += self._id3_header_length()
        self.end -= self._id3_trailer_length()

    def _id3_trailer_length(self):
        try:
            self.file.seek(-128, io.SEEK_END)
            idata = self.file.read(3)
            if idata == "TAG":
                return 128
        except IOError:
            pass
        return 0

    def _id3_header_length(self):
        try:
            # technically an insize=0 tag is invalid, but we skip it anyway
            self.file.seek(0)
            idata = self.file.read(10)
            id3, insize = struct.unpack('>3sxxx4s', idata)
            insize = BitPaddedInt(insize)
            if id3 == 'ID3' and 0 <= insize <= self.end - 10:
                return insize + 10
        except (IOError, struct.error):
            pass
        return 0

    def data(self):
        self.file.seek(self.start)
        return self.file.read(self.end - self.start)