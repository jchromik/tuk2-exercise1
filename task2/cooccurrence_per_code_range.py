"""For each ICD9 code range,
see https://en.wikipedia.org/wiki/List_of_ICD-9_codes,
find out which two of ICD9 codes occur together most often.
Cooccurrence is defined as same patient and same year."""

from collections import defaultdict

import json
import pyhdb

 # see: https://en.wikipedia.org/wiki/List_of_ICD-9_codes for ICD9 code ranges

RANGE_STARTS = [
    1, 140, 240, 280, 290, 320, 390, 460, 520, 580, 630, 680, 710, 740, 760,
    780, 800]

RANGE_NAMES = [
    "Malformed ICD9Code",
    "001–139: infectious and parasitic diseases",
    "140–239: neoplasms",
    "240–279: endocrine, nutritional and metabolic diseases, and immunity disorders",
    "280–289: diseases of the blood and blood-forming organs",
    "290–319: mental disorders",
    "320–389: diseases of the nervous system and sense organs",
    "390–459: diseases of the circulatory system",
    "460–519: diseases of the respiratory system",
    "520–579: diseases of the digestive system",
    "580–629: diseases of the genitourinary system",
    "630–679: complications of pregnancy, childbirth, and the puerperium",
    "680–709: diseases of the skin and subcutaneous tissue",
    "710–739: diseases of the musculoskeletal system and connective tissue",
    "740–759: congenital anomalies",
    "760–779: certain conditions originating in the perinatal period",
    "780–799: symptoms, signs, and ill-defined conditions",
    "800–999: injury and poisoning",
    "E: external causes of injury",
    "V: supplemental classification"]

def main():
    """The main method. Called at the end of this file.
    Processes query and outputs results.
    """
    diagnoses_all = query_diagnoses()

    for i in range(0, len(RANGE_NAMES)):
        diagnoses_ranged = [
            diagnosis
            for diagnosis
            in diagnoses_all if code_to_range(diagnosis[2]) == i]
        cooccurrences = count_cooccurrences(diagnoses_ranged).items()
        cooccurrences = sorted(cooccurrences, key=lambda x: x[1], reverse=True)
        if cooccurrences:
            code1 = cooccurrences[0][0][0]
            code2 = cooccurrences[0][0][1]
            count = cooccurrences[0][1]
            print(RANGE_NAMES[i])
            print("\t" + code1 + " and " + code2 + " appearing together " + str(count) + " times.")


def query_diagnoses():
    """Queries the database returning a list of tuples:
    (PatientGuid, StartYear, ICD9Code)
    """
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

    return cursor.fetchall()

def count_cooccurrences(diagnoses):
    """Counts how often ICD9 codes occur together (same patient, same year)."""
    cooccurrences = defaultdict(int)
    pair_gen = (
        (d1[2], d2[2])
        for d1 in diagnoses
        for d2 in diagnoses
        if d1[0] == d2[0] and d1[1] == d2[1] and d1[2] < d2[2])
    for pair in pair_gen:
        cooccurrences[pair] += 1
    return cooccurrences


def code_to_prefix(icd9code):
    """Extracts the prefix (part before the dot) of an ICD9 code.
    Examples:
        410.2 --> 410
        V70.0 --> V70
        120   --> 120
    """
    if "." in icd9code:
        return icd9code.split(".")[0]
    return icd9code

def prefix_to_range(icd9prefix):
    """Converts an ICD9 code prefix to its range number.
    See RANGE_NAMES for a mapping of range numbers and names.
    """
    if "E" in icd9prefix.upper():
        return 18
    if "V" in icd9prefix.upper():
        return 19

    try:
        numeric_prefix = int(icd9prefix)
    except ValueError:
        return 0

    for i in range(0, len(RANGE_STARTS)):
        if RANGE_STARTS[i] > numeric_prefix:
            return i

    return len(RANGE_STARTS)

def code_to_range(icd9code):
    """Convenience"""
    return prefix_to_range(code_to_prefix(icd9code))

main()
