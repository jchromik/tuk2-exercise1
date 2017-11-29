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
    SELECT "DiagnosisDescription", COUNT("DiagnosisDescription") AS "occurences"
    FROM "TUKGRP7"."Diagnosis"
    GROUP BY "DiagnosisDescription"
    ORDER BY "occurences" DESC)
    """)

        cursor.execute("""
    SELECT "DiagnosisDescription", COUNT("DiagnosisDescription") AS "occurences", "YearOfBirth"
    FROM "TUKGRP7"."Diagnosis", "TUKGRP7"."Patient"
    WHERE "TUKGRP7"."Diagnosis"."PatientGuid" = "TUKGRP7"."Patient"."PatientGuid" AND "TUKGRP7"."Diagnosis"."DiagnosisDescription" = 'Cough'
    GROUP BY "DiagnosisDescription", "YearOfBirth"
    ORDER BY "YearOfBirth" ASC
        """)

        diseases = cursor.fetchall()
        print(diseases)

        return diseases
