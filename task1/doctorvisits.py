import pyhdb

class DoctorVisits:

    VISIT_VIEW_PREFIX = """
        CREATE VIEW "Visits" AS (
        SELECT T."PatientGuid", COUNT(T."TranscriptGuid") AS "Visits"
        FROM
           "TUKGRP7"."Transcript" AS T INNER JOIN "TUKGRP7"."Patient" AS P
            ON T."PatientGuid" = P."PatientGuid"
        """

    VISIT_VIEW_SUFFIX = """GROUP BY T."PatientGuid");"""

    SELECT_STATEMENT = """
        SELECT "State", AVG("Visits")
        FROM
            "TUKGRP7"."Visits" AS V INNER JOIN "TUKGRP7"."Patient" AS P
            ON V."PatientGuid" = P."PatientGuid"
        GROUP BY "State"
        """

    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.column_name = "Visits"
        self.legend_name = "Average Visits"
        self.title = "Doctor Visits per State"

    def generate(self, gender=None):
        cursor = self.db_conn.cursor()
        try:
            cursor.execute("""DROP VIEW "TUKGRP7"."Visits";""")
        except pyhdb.exceptions.DatabaseError:
            pass

        cursor.execute(
            DoctorVisits.VISIT_VIEW_PREFIX +
            self.where_clause('M', 2000, 2012) +
            DoctorVisits.VISIT_VIEW_SUFFIX)

        cursor.execute(DoctorVisits.SELECT_STATEMENT)

        visits = cursor.fetchall()
        visits = list(map(lambda tuple: (tuple[0], float(tuple[1])), visits))
        return visits

    def where_clause(self, gender=None, year_start=None, year_end=None):
        result = "WHERE 1 = 1"
        if gender:
            result += " AND P.\"Gender\" LIKE '" + gender + "'"
        if year_start:
            result += " AND T.\"VisitYear\" >= " + str(year_start)
        if year_end:
            result += " AND T.\"VisitYear\" <= " + str(year_end)
        return result + "\n"
            