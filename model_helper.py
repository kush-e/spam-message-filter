import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def save(model, path='ai/model.p'):
    with open(path, 'wb') as f:
        pickle.dump(model,f)
    return True


def load(path='ai/model.p'):
    with open(path,'rb') as f:
        return pickle.load(f)
    