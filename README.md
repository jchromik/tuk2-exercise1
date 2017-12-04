
# TuK2 Winter Term 2017 / 2018: Exercise 1

## Task 1

> Load practice fusion CSV files into HANA as column tables
>
> Geospatial analyses: KPI per state (implemented as interactive map)
> - Number of patients, number of doctor visits
>   - Absolute numbers
>   - Relative to population of state
> - Average BMI (body mass index)
> - Smoker status
> - ...
> - Filterable by year and gender 

To make it run do the following:

1. `cp db-conf.sample.json db-conf.json`
2. Change password in `db-conf.json`
3. Change directory: `cd task1`
4. Run `python generate-map.py`
5. Have a look at the beautiful `map.html`

Enjoy :-)

TODO: Complete task

## Task 2

### Step 1

> Determine the most common diseases and their distributions among age groups (line chart for 10 most common diagnoses)

This is done by `most-common-diseases.py`. Run `python3 most-common-diseases.py`.

### Step 2

> Determine the overall 10 most common diseases that appear together
> - We assume that two diseases appear together if they are diagnosed for the same patient in the same year
> - The analysis should be done via a single SQL statement
> - Please report the runtime of the query
> - Read about ICD-9 codes (you may want to group diseases)

The SQL queries can be found in `diseases_co-occurrence_icd9.sql` (diseased referenced by ICD9 code) and `diseases_co-occurrence_description.sql` (diseased referenced by description). These files also contain the runtime of the queries as a comment. Results are to be found in the corresponding CSV files.

### Step 3

> Determine the two most common diseases per ICD-9 code range ([https://en.wikipedia.org/wiki/List_of_ICD-9_codes](https://en.wikipedia.org/wiki/List_of_ICD-9_codes)) that appear together

TODO: How does this differ from step 2?

## Task 3

> Working on aggregated data:
>
> - Calculate the doctor visits per age group (0-9, 10-19, etc.) and visualize the data points. Further, use an interpolation method to estimate the doctor visits for each age. Compare the interpolated data with the actual data and calculate the mean squared error (MSE) & visualize.
>
> Model the blood pressure using linear regression:
> - Use the explanatory variables: smoking status, BMI, age (, and ...)
> - Determine the coefficient of determination R 2 for your regression.

TODO