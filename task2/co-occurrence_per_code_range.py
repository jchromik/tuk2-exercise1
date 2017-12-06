from collections import defaultdict

import json
import pyhdb

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

    for i in range(0, 20):
        diagnoses_ranged = [diagnosis for diagnosis in diagnoses_all if code_to_range(diagnosis[2]) == i]
        print(count_cooccurrences(diagnoses_ranged))

    # TODO: go on here and return most often cooccurrences

def count_cooccurrences(diagnoses):
    cooccurrences = defaultdict(int)
    for pair in ((d1[2],d2[2]) for d1 in diagnoses for d2 in diagnoses if d1[0] == d2[0] and d1[1] == d2[1] and d1[2] < d2[2]):
        cooccurrences[pair] += 1
    return cooccurrences


def code_to_prefix(icd9code):
    if "." in icd9code:
        return icd9code.split(".")[0]
    return icd9code

def prefix_to_range(icd9prefix):
    # see: https://en.wikipedia.org/wiki/List_of_ICD-9_codes for named ranges
    if "E" in icd9prefix.upper():
        return 18
    if "V" in icd9prefix.upper():
        return 19
    range_starts = [
        1, 140, 240, 280, 290, 320, 390, 460, 520, 580, 630, 680, 710, 740,
        760, 780, 800]
    try: 
        numeric_prefix = int(icd9prefix)
    except ValueError:
        return 0
    for i in range(0,len(range_starts)):
        if range_starts[i] > numeric_prefix:
            return i
    return len(range_starts)

def code_to_range(icd9code):
    return prefix_to_range(code_to_prefix(icd9code))

main()
