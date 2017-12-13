import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression

class LinearRegressor:

    def train(data):

        other_data = []           #smoking status, bmi and age
        systolicBP_data = []      #systolic blood pressure
        diastolicBP_data = []     #diastolic blood pressure

        for idx in range (0, len(data)):
            tuple = (data[idx][0], data[idx][1], data[idx][2])
            other_data.append(tuple)
            systolicBP_data.append(data[idx][3])
            diastolicBP_data.append(data[idx][4])

        ######################### systolic #################################################################
        #split data in test- and training data:
        other_train, other_test, bp_train, bp_test = train_test_split(other_data, systolicBP_data, test_size=0.10, random_state=0)

        model = LinearRegression()
        model.fit(other_train, bp_train)

        # predict on test data
        bp_pred = model.predict(other_test)     #predict the blood pressure through other data

        indices = np.arange(0, len(bp_test), 1)

        ######################### Plot all data ############################################################
        plt.title('Predicted vs real blood pressure (systolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=3, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=2, color='blue', marker='o', label = 'predicted data')
        plt.legend(loc='lower center')
        plt.show()


        print('_________________________________________________')
        print("R^2 for systolic blood pressure: ", r2_score(bp_test, bp_pred))
        print('_________________________________________________')

        ######################### Zoom in: Plot first 100 of data ###########################################
        indices = indices[:100]
        bp_test = bp_test[:100]
        bp_pred = bp_pred[:100]

        plt.title('Predicted vs real blood pressure (systolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=9, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=9, color='blue', marker='o', label = 'predicted data')
        plt.legend(loc='lower center')
        plt.show()

        ######################### diastolic #################################################################
        other_train, other_test, bp_train, bp_test = train_test_split(other_data, diastolicBP_data, test_size=0.10, random_state=0)

        model = LinearRegression()
        model.fit(other_train, bp_train)

        bp_pred = model.predict(other_test)     #predict the blood pressure through other data

        indices = np.arange(0, len(bp_test), 1)

        print('_________________________________________________')
        print("R^2 for diastolic blood pressure: ", r2_score(bp_test, bp_pred))
        print('_________________________________________________')

        ######################### Plot all data #############################################################
        plt.title('Predicted vs real blood pressure (diastolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=3, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=2, color='blue', marker='o', label='predicted data')
        plt.legend(loc='lower center')
        plt.show()

        ######################### Zoom in: Plot first 100 of data ###########################################
        indices = indices[:100]
        bp_test = bp_test[:100]
        bp_pred = bp_pred[:100]

        plt.title('Predicted vs real blood pressure (diastolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=9, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=9, color='blue', marker='o', label='predicted data')
        plt.legend(loc='lower center')
        plt.show()

        return None




    #use even more data
    def trainExtra(data):

        other_data = []           #smoking status, bmi and age
        systolicBP_data = []      #systolic blood pressure
        diastolicBP_data = []     #diastolic blood pressure
        for idx in range (0, len(data)):
            tuple = (data[idx][0], data[idx][1], data[idx][2], data[idx][3], data[idx][5], data[idx][6],
                     data[idx][7])
            other_data.append(tuple)
            systolicBP_data.append(data[idx][8])
            diastolicBP_data.append(data[idx][9])

        ######################### systolic #################################################################
        #split data in test- and training data:
        other_train, other_test, bp_train, bp_test = train_test_split(other_data, systolicBP_data, test_size=0.10, random_state=0)

        model = LinearRegression()
        model.fit(other_train, bp_train)

        # predict on test data
        bp_pred = model.predict(other_test)     #predict the blood pressure through other data

        indices = np.arange(0, len(bp_test), 1)

        ######################### Plot all data ############################################################
        plt.title('Predicted vs real blood pressure (systolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=3, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=2, color='blue', marker='o', label = 'predicted data')
        plt.legend(loc='lower center')
        plt.show()


        print('_________________________________________________')
        print("R^2 for systolic blood pressure: ", r2_score(bp_test, bp_pred))
        print('_________________________________________________')

        ######################### Zoom in: Plot first 100 of data ###########################################
        indices = indices[:100]
        bp_test = bp_test[:100]
        bp_pred = bp_pred[:100]

        plt.title('Predicted vs real blood pressure (systolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=9, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=9, color='blue', marker='o', label = 'predicted data')
        plt.legend(loc='lower center')
        plt.show()

        ######################### diastolic #################################################################
        other_train, other_test, bp_train, bp_test = train_test_split(other_data, diastolicBP_data, test_size=0.10, random_state=0)

        model = LinearRegression()
        model.fit(other_train, bp_train)

        bp_pred = model.predict(other_test)     #predict the blood pressure through other data

        indices = np.arange(0, len(bp_test), 1)

        print('_________________________________________________')
        print("R^2 for diastolic blood pressure: ", r2_score(bp_test, bp_pred))
        print('_________________________________________________')

        ######################### Plot all data #############################################################
        plt.title('Predicted vs real blood pressure (diastolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=3, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=2, color='blue', marker='o', label='predicted data')
        plt.legend(loc='lower center')
        plt.show()

        ######################### Zoom in: Plot first 100 of data ###########################################
        indices = indices[:100]
        bp_test = bp_test[:100]
        bp_pred = bp_pred[:100]

        plt.title('Predicted vs real blood pressure (diastolic)')
        plt.xlabel('data')
        plt.ylabel('blood pressure')
        plt.scatter(indices, bp_test, s=9, color='r', marker='o', label='real data')
        plt.scatter(indices, bp_pred, s=9, color='blue', marker='o', label='predicted data')
        plt.legend(loc='lower center')
        plt.show()

        return None
