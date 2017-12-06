import matplotlib.pyplot as plt
import json
import pyhdb
import numpy as np
from doctorvisits import Visits
from interpolation import Interpolator
from bloodPressure import BloodPressure
from linearRegression import LinearRegressor
from math import sqrt

with open("../db-conf.json") as db_conf_file:
    db_conf = json.load(db_conf_file)

connection = pyhdb.connect(
    host=db_conf["host"],
    port=db_conf["port"],
    user=db_conf["user"],
    password=db_conf["password"],
)

############################# visualize age groups ######################################
def interpolation_task():
    print("Calculate and interpolate doctor visits for patients of different age")
    gen = Visits(connection)
    data = gen.generate()

    ageGroups = []
    startYear = 10

    #youngest person is 15, oldest is 90
    for ageGroup in range(0, 9):   #10-99 years old in 9 age groups
        endYear = startYear + 9
        visits = 0

        for x in range(0, len(data)):
            if (startYear < data[x][0] < endYear):
                visits = visits + data[x][1]

        tup1 = (ageGroup, startYear, visits)
        ageGroups.append(tup1)
        startYear = startYear + 10

    indices = []
    ages = []
    numberOfVisits = []
    ageGroupTags = []

    for x in range(0, len(ageGroups)):
        indices.append(ageGroups[x][0])
        ages.append(ageGroups[x][1])
        numberOfVisits.append(ageGroups[x][2])
        ageGroupTags.append(str(ageGroups[x][1]) + "-" + str(ageGroups[x][1]+9))

    indices = np.array(indices)
    ages = np.array(ages)
    numberOfVisits = np.array(numberOfVisits)

    ind = np.arange(9)  # the x locations for the groups
    width = 0.45       # the width of the bars

    plt.title('doctor visits per age groups')
    plt.xlabel('age groups')
    plt.ylabel('number of visits')
    my_xticks = ageGroupTags
    plt.xticks(indices, my_xticks)
    plt.bar(ind, numberOfVisits, 0.35, align='center')

    plt.show()

    ################### interpolate and compare with real data ######################
    actualData = []

    for x in range(0, len(data)):
            actualData.append(data[x][1])

    interpolatedData = Interpolator.interpolate(ages, numberOfVisits)
    mse = Interpolator.mean_squared_error(interpolatedData, actualData)

    print('_______________________________')
    print('Mean Squared Error: ')
    print(mse)
    print('Root Mean Squared Error: ')
    print(sqrt(mse))
    print('_______________________________')


############################# get smoking status, bmi, age and blood pressures ######################################
def linear_regression_task():
    gen = BloodPressure(connection)
    data = gen.generate()
    print("Predict blood pressure through Smoking Status, BMI and Age")
    LinearRegressor.train(data)

############################# get smoking status, bmi, age, height, weight, RespiratoryRate, HeartRate, temperature and blood pressures ######################################
def linear_regression_task_extra():
    gen = BloodPressure(connection)
    data = gen.generateExtra()
    print("Predict blood pressure through Smoking Status, BMI, Age, Height, Weight, Respiratory Rate, Heart Rate and Temperature")
    LinearRegressor.trainExtra(data)


interpolation_task()
linear_regression_task()
linear_regression_task_extra()
