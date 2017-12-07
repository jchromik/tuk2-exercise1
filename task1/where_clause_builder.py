def build(gender=None, start_year=None, end_year=None):
    result = "WHERE 1 = 1"
    if gender:
        result += " AND P.\"Gender\" LIKE '" + gender[0].upper() + "'"
    if start_year:
        result += " AND T.\"VisitYear\" >= " + str(start_year)
    if end_year:
        result += " AND T.\"VisitYear\" <= " + str(end_year)
    return result + "\n"
