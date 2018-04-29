import pickle
import numpy as np


def read_pickle(step):
    with open('D:\\Python\Agent\\pickle\\tick{}.pickle'.format(step), 'rb') as handle:
        return pickle.load(handle)