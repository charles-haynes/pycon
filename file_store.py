import hashlib
import io

__author__ = 'chaynes'

class DuplicateEntry(BaseException):
    pass


class FileStore(object):
    def __init__(self, hasher=hashlib.md5):
        self.hasher = hasher
        self.hash_set = set()

    def Add(self, name):
        if self.Hash(name) in self.hash_set:
            raise DuplicateEntry
        self.hash_set.add(self.Hash(name))

    def Hash(self, name):
        f = io.open(name, 'rb')
        return self.hasher(f.readall())

    def Hashes(self):
        return self.hash_set