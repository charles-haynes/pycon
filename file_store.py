import hashlib
import io
import mp3_file

__author__ = 'chaynes'

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
            mp3 = mp3_file.Mp3File(f)
            return self.hasher(mp3.data())

    def Hashes(self):
        return self.hash_set