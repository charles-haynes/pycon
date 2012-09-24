import hashlib
import io

__author__ = 'chaynes'

class DuplicateEntry(BaseException):
    pass


class FileDictionary(object):
    def __init__(self):
        self.file_dictionary = {}

    def Add(self, name):
        if name in self.file_dictionary:
            raise DuplicateEntry
        self.file_dictionary[name] = self.Hash(name)

    def Hash(self, name):
        f = io.open(name, 'rb')
        return hashlib.md5(f.readall())

    def Dict(self):
        return self.file_dictionary