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

age = []
occurences = []

for x in range(0, len(data)):
    occurences.append((data[x][1]))
    age.append(data[x][2])

age = np.array(age)
occurences = np.array(occurences)

plt.title('10 most common diseases')
plt.xlabel('age')
plt.ylabel('patients')
plt.plot(age, occurences, 'g-', label=data[0][0])
leg = plt.legend(loc='right')

#plt.xticks(x, diseases)
#plt.axis([0, 10, 0, 100])

plt.show()
