from os.path import isfile, join, abspath, dirname
from os import listdir

def get_train_files():
    my_path = abspath(dirname(__file__))
    train_dir = join(my_path, 'train/')
    onlyfiles = [train_dir + f for f in listdir(train_dir) if isfile(join(train_dir, f))]
    return onlyfiles