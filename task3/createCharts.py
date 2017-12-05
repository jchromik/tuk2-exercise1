import matplotlib.pyplot as plt
import json
import pyhdb
import numpy as np
from doctorvisits import Visits
from interpolation import Interpolator

with open("../db-conf.json") as db_conf_file:
    db_conf = json.load(db_conf_file)

currentYear = 2018

connection = pyhdb.connect(
    host=db_conf["host"],
    port=db_conf["port"],
    user=db_conf["user"],
    password=db_conf["password"],
)

############################# visualize age groups ######################################
gen = Visits(connection)
data = gen.generate()

ageGroups = []
startYear = 20

#youngest person is 23, oldest is 95
for ageGroup in range(0, 8):   #20-100 years old in 8 age groups
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

ind = np.arange(8)  # the x locations for the groups
width = 0.35       # the width of the bars

plt.title('doctor visits per age groups')
plt.xlabel('age groups')
plt.ylabel('number of visits')
my_xticks = ageGroupTags
plt.xticks(indices, my_xticks)
plt.bar(ind, numberOfVisits, 0.35, align='center')

plt.show()


################### interpolate and compare with real data######################
actualData = []

for x in range(0, len(data)):
    if 23 < data[x][0] < 95:                #we only created interpolated data between ages 24 and 94
        actualData.append(data[x][1])

interpolatedData = Interpolator.interpolate(ages, numberOfVisits)
mse = Interpolator.mean_squared_error(interpolatedData, actualData)
print(mse)


