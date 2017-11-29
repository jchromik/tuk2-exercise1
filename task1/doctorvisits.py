class DoctorVisits:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.column_name = "Visits"
        self.legend_name = "Average Visits"
        self.title = "Doctor Visits per State"

    def generate(self):
        cursor = self.db_conn.cursor()
        cursor.execute("""
    DROP VIEW "TUKGRP7"."Visits"
    """)
        cursor.execute("""
    CREATE VIEW "Visits" AS (
    SELECT "PatientGuid", COUNT("TranscriptGuid") AS "Visits"
    FROM "TUKGRP7"."Transcript"
    GROUP BY "PatientGuid")
    """)
        cursor.execute("""
    SELECT "State", AVG("Visits")
    FROM "TUKGRP7"."Visits", "TUKGRP7"."Patient"
    WHERE "TUKGRP7"."Visits"."PatientGuid" = "TUKGRP7"."Patient"."PatientGuid"
    GROUP BY "State"
    """)
        visits = cursor.fetchall()
        visits = list(map(lambda tuple: (tuple[0], float(tuple[1])), visits))
        return visits
