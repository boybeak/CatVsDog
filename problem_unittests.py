import os
import numpy as np
import tensorflow as tf
import random
from unittest.mock import MagicMock


def test_folder_path(train_folder_path):
    assert train_folder_path is not None, 'train_folder_path not set'
    assert train_folder_path[-1] != '/', 'The "/" shouldn\'t be added to the end of the path.'
    assert os.path.exists(train_folder_path), 'path not found ' + train_folder_path
    assert os.path.isdir(train_folder_path), '{} is not a folder.'.format(os.path.basename(train_folder_path))

    train_files = [train_folder_path + '/data_batch_' + str(batch_id) for batch_id in range(1, 6)]
    other_files = [train_folder_path + '/batches.meta', train_folder_path + '/test_batch']
    missing_files = [path for path in train_files + other_files if not os.path.exists(path)]

    assert not missing_files, 'Missing files in directory: {}'.format(missing_files)

    print('All files found!')
