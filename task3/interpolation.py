import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from sklearn.metrics import mean_squared_error

class Interpolator:

    def interpolate(ages, numberOfVisits):

        averageAges = []

        for i in range(9):
            if i == 0:
                averageAges.append(ages[i]+5)
            elif i == 8:
                averageAges.append(ages[i])
            else: averageAges.append(ages[i]+4)

        averageVisits = []

        for i in range(9):                               #there are normally 10 ages in an age group (5 in the first and only 1 in the last)
            if i == 0:
                averageVisits.append((numberOfVisits[i]/5)/2)
            elif i == 8:
                averageVisits.append(numberOfVisits[i])
            else: averageVisits.append(numberOfVisits[i]/10)

        #f = interpolate.Akima1DInterpolator(averageAges, averageVisits)
        #f = interpolate.interp1d(averageAges, averageVisits)
        #f = interpolate.KroghInterpolator(averageAges, averageVisits)
        #f = interpolate.PchipInterpolator(averageAges, averageVisits)
        f = interpolate.CubicSpline(averageAges, averageVisits)                     #best mse

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
