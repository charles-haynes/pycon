import file_store
import os
import sys

__author__ = 'chaynes'

def find_duplicates(root_dir):
    file_dict = file_store.FileStore()
    for dir_path, dir_list, file_list in os.walk(root_dir):
        for filename in file_list:
            file_dict.Add(os.path.join(dir_path, filename))

if __name__ == '__main__':
    f_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    find_duplicates(f_path)
