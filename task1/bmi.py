import where_clause_builder

class BMI:

    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.column_name = "BMI"
        self.legend_name = "Average BMI"
        self.title = "BMI per State"

    def generate(self, gender=None, start_year=None, end_year=None):
        cursor = self.db_conn.cursor()
        cursor.execute("""
            SELECT P."State", AVG("BMI")
            FROM
                "TUKGRP7"."Patient" AS P INNER JOIN "TUKGRP7"."Transcript" AS T
                ON P."PatientGuid" = T."PatientGuid" """ +
            where_clause_builder.build(gender, start_year, end_year) +
            "GROUP BY P.\"State\"")

        bmi = cursor.fetchall()
        bmi = list(map(lambda tuple: (tuple[0], float(tuple[1])), bmi))

        return bmi
