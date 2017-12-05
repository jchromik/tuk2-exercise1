class Visits:
    def __init__(self, db_conn):
        self.db_conn = db_conn

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
    SELECT "YearOfBirth", Sum("Visits")
    FROM "TUKGRP7"."Visits", "TUKGRP7"."Patient"
    WHERE "TUKGRP7"."Visits"."PatientGuid" = "TUKGRP7"."Patient"."PatientGuid"
    GROUP BY "YearOfBirth", "Visits"
            """)

        cursor.execute("""
    SELECT 2017 - "Patient"."YearOfBirth" as "age", COUNT("Transcript"."PatientGuid") as "doctorVisits"
    FROM "TUKGRP7"."Patient"
    INNER JOIN "TUKGRP7"."Transcript" ON "Patient"."PatientGuid"="Transcript"."PatientGuid"
    GROUP BY 2017 - "Patient"."YearOfBirth"
    ORDER BY 2017 - "Patient"."YearOfBirth" ASC
                """)

        visits = cursor.fetchall()
        #visits = list(map(lambda tuple: (tuple[0], float(tuple[1])), visits))
        return visits
