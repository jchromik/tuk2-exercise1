import matplotlib.pyplot as plt
import json
import pyhdb
import numpy as np


def main():
    with open("../db-conf.json") as db_conf_file:
        db_conf = json.load(db_conf_file)

    connection = pyhdb.connect(
        host=db_conf["host"],
        port=db_conf["port"],
        user=db_conf["user"],
        password=db_conf["password"],
    )

    data = query_database(connection)
    
    plot(data)

def query_database(db_conn):
    cursor = db_conn.cursor()

    cursor.execute("""DROP VIEW "TUKGRP7"."Top10Diseases";""")

    cursor.execute("""
        CREATE VIEW "Top10Diseases" AS (
        SELECT "ICD9Code", COUNT("DiagnosisGuid") AS "Occurences"
        FROM "TUKGRP7"."Diagnosis"
        GROUP BY "ICD9Code"
        ORDER BY "Occurences" DESC
        LIMIT 10);
        """)
    cursor.execute("""
        SELECT
            D."ICD9Code",
            P."YearOfBirth",
            COUNT(D."PatientGuid") AS "Occurences"
        FROM
            "TUKGRP7"."Diagnosis" AS D INNER JOIN "TUKGRP7"."Patient" AS P
            ON D."PatientGuid" = P."PatientGuid"
        WHERE "ICD9Code" IN (SELECT "ICD9Code" FROM "TUKGRP7"."Top10Diseases")
        GROUP BY D."ICD9Code", P."YearOfBirth"
        ORDER BY D."ICD9Code", P."YearOfBirth" ASC;
        """)
   
    diseases = cursor.fetchall()
    print(diseases)
    return diseases

def plot(data):
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

main()