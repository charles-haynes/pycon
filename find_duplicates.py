import file_enumerator
import file_store
import os
import sys

__author__ = 'chaynes'

def main(f_path=os.getcwd()):
    store = file_store.FileStore(os.unlink)
    for file in file_enumerator.files(f_path):
        store.Add(file)

if __name__ == '__main__':
    main(*sys.argv[1:])
