import json
import pyhdb
import re

def main():
    with open("../db-conf.json") as db_conf_file:
        db_conf = json.load(db_conf_file)

    connection = pyhdb.connect(
        host=db_conf["host"],
        port=db_conf["port"],
        user=db_conf["user"],
        password=db_conf["password"])

    cursor = connection.cursor()

    cursor.execute("""
        SELECT "PatientGuid", "StartYear", "ICD9Code"
        FROM "TUKGRP7"."Diagnosis"
        WHERE "StartYear" != 0;
        """)

    diagnoses_all = cursor.fetchall()
    diagnoses_ranged = []

    for i in range(0,20):
        diagnoses_ranged.append(list(filter(
            lambda tuple: code_to_range(tuple[2]) == i, diagnoses_all)))

    # diagnoses_ranged has the following format:
    # [   list_with_range_0_diagnoses,
    #     list_with_range_1_diagnoses,
    #     ...,
    #     list_with_range_19_diagnses ]
    # see: https://en.wikipedia.org/wiki/List_of_ICD-9_codes for named ranges

    # TODO: go on here and count co-occurrences

def code_to_prefix(icd9code):
    if "." in icd9code:
        return icd9code.split(".")[0]
    else:
        return icd9code

def prefix_to_range(icd9prefix):
    if "E" in icd9prefix.upper():
        return 18
    if "V" in icd9prefix.upper():
        return 19
    range_starts = [
        1, 140, 240, 280, 290, 320, 390, 460, 520, 580, 630, 680, 710, 740,
        760, 780, 800]
    try: 
        numeric_prefix = int(icd9prefix)
    except:
        return 0
    for i in range(0,len(range_starts)):
        if range_starts[i] > numeric_prefix:
            return i
    return len(range_starts)

def code_to_range(icd9code):
    return prefix_to_range(code_to_prefix(icd9code))

main()