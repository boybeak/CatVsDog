from os.path import isfile, join, abspath, dirname
from os import listdir

def get_files_of_floder(folder):
    my_path = abspath(dirname(__file__))
    train_dir = join(my_path, folder)
    onlyfiles = [train_dir + f for f in listdir(train_dir) if isfile(join(train_dir, f))]
    return onlyfiles

def get_train_files():
    return get_files_of_floder('train/')

def get_test_files():
    return get_files_of_floder('test/')