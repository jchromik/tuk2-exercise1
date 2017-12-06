import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


class Interpolator:

    def interpolate(ages, numberOfVisits):
        averageAges = [x+4 for x in ages]                   #the average person in group 10-19 is 14
        averageVisits = [x/10 for x in numberOfVisits]      #there are 10 ages in an age group

        f = interpolate.Akima1DInterpolator(averageAges, averageVisits)    #best mse
        #f = interpolate.interp1d(averageAges, averageVisits)
        #f = interpolate.KroghInterpolator(averageAges, averageVisits)
        #f = interpolate.PchipInterpolator(averageAges, averageVisits)
        #f = interpolate.CubicSpline(averageAges, averageVisits)

        allAges = np.arange(15, 91, 1)    #values are from 15 to 90

        interpolatedVisits = f(allAges)

        plt.title('Interpolated doctor visits per age')
        plt.xlabel('age')
        plt.ylabel('number of visits')
        plt.plot(averageAges, averageVisits, 'ro', label = 'average patient in age group')
        plt.plot(allAges, interpolatedVisits, 'b-', label = 'interpolated data')
        plt.legend(loc='lower center')
        plt.show()
        return interpolatedVisits


    def mean_squared_error(interpolatedData, actualData):
        allAges = np.arange(15, 91, 1)    #values are from 15 to 90

        plt.title('Interpolated vs real doctor visits per age')
        plt.xlabel('age')
        plt.ylabel('number of visits')
        plt.plot(allAges, actualData, 'ro', label = 'real data')
        plt.plot(allAges, interpolatedData, 'b-', label = 'interpolated data')
        plt.legend(loc='lower center')
        plt.show()
        mse = np.mean((actualData - interpolatedData) ** 2)
        return mse
