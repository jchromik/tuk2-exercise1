import json


class Diseases:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.column_name = "Patients"
        self.legend_name = "#Patients / #Inhabitants in Percent"
        self.title = "Percentage of Patients per State"


    def generate(self):
        cursor = self.db_conn.cursor()
        cursor.execute("""
            DROP VIEW "TUKGRP7"."Top10Diseases"
            """)

        cursor.execute("""
            CREATE VIEW "Top10Diseases" AS (
            SELECT "ICD9Code", COUNT("DiagnosisGuid") AS "Occurences"
            FROM "TUKGRP7"."Diagnosis"
            GROUP BY "ICD9Code"
            ORDER BY "Occurences" DESC
            LIMIT 10)
            """)

        cursor.execute("""
            SELECT D."ICD9Code", P."YearOfBirth", COUNT(D."PatientGuid") as "Occurences"
            FROM "TUKGRP7"."Diagnosis" AS D INNER JOIN "TUKGRP7"."Patient" AS P ON D."PatientGuid" = P."PatientGuid"
            WHERE "ICD9Code" IN (SELECT "ICD9Code" FROM "TUKGRP7"."Top10Diseases")
            GROUP BY D."ICD9Code", P."YearOfBirth"
            ORDER BY D."ICD9Code", P."YearOfBirth" ASC
            """)

    #     cursor.execute("""
    # SELECT "DiagnosisDescription", COUNT("DiagnosisDescription") AS "occurences", "YearOfBirth"
    # FROM "TUKGRP7"."Diagnosis", "TUKGRP7"."Patient"
    # WHERE "TUKGRP7"."Diagnosis"."PatientGuid" = "TUKGRP7"."Patient"."PatientGuid" AND "TUKGRP7"."Diagnosis"."DiagnosisDescription" = 'Cough'
    # GROUP BY "DiagnosisDescription", "YearOfBirth"
    # ORDER BY "YearOfBirth" ASC
    #     """)

        diseases = cursor.fetchall()
        print(diseases)

        return diseases
