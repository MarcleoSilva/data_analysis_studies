import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import shapiro

def test_normal_distribution(data,columns_range):
    col_names = data.columns.tolist()
    for column in col_names[:columns_range]:
        stat, p = shapiro(data[column])
        print(column)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        if p <= 0.05:
            print("Not normally distributed")
        else:
            print("Normally distributed")