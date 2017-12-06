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
    FROM "Transcript"
    GROUP BY "PatientGuid")
    """)

        cursor.execute("""
    SELECT "YearOfBirth", Sum("Visits")
    FROM "Visits", "Patient"
    WHERE "Visits"."PatientGuid" = "Patient"."PatientGuid"
    GROUP BY "YearOfBirth", "Visits"
            """)

        cursor.execute("""
    SELECT "Transcript"."VisitYear" - "Patient"."YearOfBirth" as "age", COUNT("Transcript"."PatientGuid") as "doctorVisits"
    FROM "Patient"
    INNER JOIN "Transcript" ON "Patient"."PatientGuid"="Transcript"."PatientGuid"
    WHERE "Transcript"."VisitYear" != 0
    GROUP BY "Transcript"."VisitYear" - "Patient"."YearOfBirth"
    ORDER BY "Transcript"."VisitYear" - "Patient"."YearOfBirth" ASC
    
                """)

        visits = cursor.fetchall()
        return visits
