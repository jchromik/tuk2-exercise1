import matplotlib.pyplot as plt
import json
import pyhdb
import numpy as np
from doctorvisits import Visits

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
    currentGroup = str(startYear) + "-" + str(endYear)
    visits = 0

    for x in range(0, len(data)):
        if (startYear < data[x][0] < endYear):
            visits = visits + data[x][1]

    tup1 = (ageGroup, currentGroup, visits)
    ageGroups.append(tup1)
    startYear = startYear + 10

indices = []
ages = []
numberOfVisits = []

for x in range(0, len(ageGroups)):
    indices.append(ageGroups[x][0])
    ages.append(ageGroups[x][1])
    numberOfVisits.append(ageGroups[x][2])

indices = np.array(indices)
ages = np.array(ages)
numberOfVisits = np.array(numberOfVisits)

ind = np.arange(8)  # the x locations for the groups
width = 0.35       # the width of the bars

plt.title('doctor visits per age groups')
plt.xlabel('age groups')
plt.ylabel('number of visits')
my_xticks = ages
plt.xticks(indices, my_xticks)
plt.bar(ind, numberOfVisits, 0.35, align='center')


plt.show()
