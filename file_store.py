import hashlib
import io
import struct
import mutagen.id3

__author__ = 'chaynes'

def get_start_end(f):
    """Find the start and end locations of the data in the file f.

    :type f: io.file
    :rtype: (start: int, end: int) starting position of data and ending position of data in the file
    """
    start = 0
    end = f.seek(0, io.SEEK_END)
    try:
    # technically an insize=0 tag is invalid, but we skip it anyway
        f.seek(start)
        idata = f.read(10)
        try:
            id3, insize = struct.unpack('>3sxxx4s', idata)
            insize = mutagen.id3.BitPaddedInt(insize)
            if id3 == 'ID3' and 0 <= insize <= end - 10:
                start = insize + 10
        except struct.error:
            pass

        f.seek(-128, 2)
        idata = f.read(3)
        if idata == "TAG":
            end -= 128

    except IOError:
        pass

    return start, end


class FileStore(object):
    def __init__(self, on_duplicate, hasher=hashlib.md5):
        self.on_duplicate = on_duplicate
        self.hasher = hasher
        self.hash_set = set()

    def Add(self, name):
        file_hash = self.Hash(name)
        if file_hash in self.hash_set:
            self.on_duplicate(name)
        else:
            self.hash_set.add(file_hash)

    def Hash(self, name):
        with io.open(name, 'rb') as f:
            start, end = get_start_end(f)
            f.seek(start)
            return self.hasher(f.read(end - start))

    def Hashes(self):
        return self.hash_set