class BloodPressure:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def generate(self):
        cursor = self.db_conn.cursor()

        cursor.execute("""
    SELECT "SmokeCode", "BMI" , "Age", "SystolicBP", "DiastolicBP"
    FROM
    (SELECT "SmokeCode","Transcript"."BMI" , "Transcript"."VisitYear" - "Birthday" AS "Age", "Transcript"."SystolicBP", "Transcript"."DiastolicBP", "Transcript"."VisitYear", "SmokingYear"
    FROM (SELECT "Patient"."PatientGuid" AS "ID", "Patient"."YearOfBirth" AS "Birthday", "PatientSmokingStatus"."EffectiveYear" AS "SmokingYear", "SmokingStatus"."NISTcode" AS "SmokeCode"
    FROM "Patient"
    INNER JOIN "PatientSmokingStatus" ON "Patient"."PatientGuid"="PatientSmokingStatus"."PatientGuid"
    INNER JOIN "SmokingStatus" ON "PatientSmokingStatus"."SmokingStatusGuid"="SmokingStatus"."SmokingStatusGuid")
    INNER JOIN "Transcript" ON "ID"="Transcript"."PatientGuid")
    WHERE "VisitYear" = "SmokingYear" AND "SystolicBP" != 0 AND "DiastolicBP" != 0
                """)

        data = cursor.fetchall()
        return data

    def generateExtra(self):
        cursor = self.db_conn.cursor()

        cursor.execute("""
    SELECT "SmokeCode", "BMI" , "Age", "Height", "Weight", "RespiratoryRate", "HeartRate", "Temperature", "SystolicBP", "DiastolicBP"
    FROM
    (SELECT "SmokeCode","Transcript"."BMI" , "Transcript"."VisitYear" - "Birthday" AS "Age", "Transcript"."Height", "Transcript"."Weight", "Transcript"."RespiratoryRate", "Transcript"."HeartRate", "Transcript"."Temperature", "Transcript"."SystolicBP", "Transcript"."DiastolicBP", "Transcript"."VisitYear", "SmokingYear"
    FROM (SELECT "Patient"."PatientGuid" AS "ID", "Patient"."YearOfBirth" AS "Birthday", "PatientSmokingStatus"."EffectiveYear" AS "SmokingYear", "SmokingStatus"."NISTcode" AS "SmokeCode"
    FROM "Patient"
    INNER JOIN "PatientSmokingStatus" ON "Patient"."PatientGuid"="PatientSmokingStatus"."PatientGuid"
    INNER JOIN "SmokingStatus" ON "PatientSmokingStatus"."SmokingStatusGuid"="SmokingStatus"."SmokingStatusGuid")
    INNER JOIN "Transcript" ON "ID"="Transcript"."PatientGuid")
    WHERE "VisitYear" = "SmokingYear" AND "SystolicBP" != 0 AND "DiastolicBP" != 0
                """)

        data = cursor.fetchall()
        return data