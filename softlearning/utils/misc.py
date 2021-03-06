import os
import random

import tensorflow as tf
import numpy as np


PROJECT_PATH = os.path.dirname(
    os.path.realpath(os.path.join(__file__, '..', '..')))


def set_seed(seed):
    seed %= 4294967294
    random.seed(seed)
    np.random.seed(seed)
    tf.compat.v1.set_random_seed(seed)
    print("Using seed {}".format(seed))


def get_host_name():
    try:
        import socket
        return socket.gethostname()
    except Exception as e:
        print("Failed to get host name!")
        return None
