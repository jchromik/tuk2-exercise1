import argparse
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from scipy import interpolate
from math import sqrt

class Interpolator:

    def interpolate(ages, numberOfVisits):
        averageAges = [x+4 for x in ages]
        averageVisits = [x/10 for x in numberOfVisits]

        #f = interpolate.interp1d(averageAges, averageVisits)
        f = interpolate.interp1d(averageAges, averageVisits)
        allAges = np.arange(24, 95, 1) #values are between 24 and 94
        interpolatedVisits = f(allAges)

        plt.plot(averageAges, averageVisits, 'ro', allAges, interpolatedVisits, 'y-')
        plt.show()
        return interpolatedVisits


    def mean_squared_error(interpolatedData, actualData):
        allAges = np.arange(24, 95, 1)  # values are between 24 and 94
        print(actualData)
        print(interpolatedData)
        plt.plot(allAges, actualData, 'r-', allAges, interpolatedData, 'y-')
        plt.show()
        mse = np.mean((actualData - interpolatedData) ** 2)
        return mse
