from .._light_labyrinth_c._light_labyrinth_c import _libwrapper
import numpy as np


def deep_tolist(array):
    if isinstance(array, list) or isinstance(array, np.ndarray):
        return [deep_tolist(elem) for elem in array]
    else:
        return float(array)
    

class LightLabyrinthLearningHistory:
    def __init__(self, accs_train, errs_train, accs_val=np.array([]), errs_val=np.array([]), calculated=None):
        self.accs_train = accs_train
        self.accs_val = accs_val
        self.errs_train = errs_train
        self.errs_val = errs_val
        if calculated is not None:
            self.calculated = calculated

    def to_dict(self):
        return {
            "accs_train" : deep_tolist(self.accs_train),
            "accs_val" : deep_tolist(self.accs_val),
            "errs_train" : deep_tolist(self.errs_train),
            "errs_val" : deep_tolist(self.errs_val)
        }

def set_random_state(state):
    _libwrapper._set_random_state(state)