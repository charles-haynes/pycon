__author__ = 'chaynes'

import os

def files(root_dir):
    for dir_path, dir_list, file_list in os.walk(root_dir):
        for filename in file_list:
            yield os.path.join(dir_path, filename)
