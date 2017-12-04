import matplotlib.pyplot as plt
import json
import pyhdb
import numpy as np
from diseases import Diseases

with open("../db-conf.json") as db_conf_file:
    db_conf = json.load(db_conf_file)

# pdb.set_trace()

connection = pyhdb.connect(
    host=db_conf["host"],
    port=db_conf["port"],
    user=db_conf["user"],
    password=db_conf["password"],
)

gen = Diseases(connection)
data = gen.generate()

yearofbirth = {}
occurences = {}

for x in range(0, len(data)):
    icd9code = data[x][0]
    if icd9code not in yearofbirth:
        yearofbirth[icd9code] = []
    if icd9code not in occurences:
        occurences[icd9code] = []
    occurences[icd9code].append((data[x][2]))
    yearofbirth[icd9code].append(data[x][1])

plt.title('10 most common diseases by ICD9-Code')
plt.xlabel('Year of Birth')
plt.ylabel('Number of Patients')

for icd9code in yearofbirth.keys():
    yearofbirth[icd9code] = np.array(yearofbirth[icd9code])
    occurences[icd9code] = np.array(occurences[icd9code])
    plt.plot(yearofbirth[icd9code], occurences[icd9code], label="ICD9: " + icd9code)
    plt.legend(loc='upper right')

plt.show()
