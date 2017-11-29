import json


class Patients:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self.column_name = "Patients"
        self.legend_name = "#Patients / #Inhabitants in Percent"
        self.title = "Percentage of Patients per State"

    def generate(self):
        cursor = self.db_conn.cursor()
        cursor.execute("""
    SELECT "State", COUNT("State")
    FROM "TUKGRP7"."Patient"
    GROUP BY "State"
    """)
        patients = cursor.fetchall()
        with open("resources/states.json") as states_data_file:
            states_data = json.load(states_data_file)
            patients = list(map(
                lambda tuple: (tuple[0], float(tuple[1])),
                patients))
            # divide by population
            patients = map(
                lambda tuple: self.divide_by_population(tuple, states_data),
                patients)
            # convert to percent
            patients = list(map(lambda tuple: ((tuple[0], tuple[1] * 100)), patients))
        return patients

    def divide_by_population(self, patient_tuple, states_data):
        matching_states = list(filter(
            lambda data: data["code"] == patient_tuple[0],
            states_data))
        if not matching_states:
            return (patient_tuple[0], 0.0)
        total_population = matching_states[0]["population"]
        return (patient_tuple[0], patient_tuple[1] / total_population)
