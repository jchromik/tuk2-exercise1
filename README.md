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
1. Change password in `db-conf.json`
1. Change directory: `cd task1`
1. Run `python3 generate-map.py [GENDER] [START_YEAR] [END_YEAR]` (`GENDER` is `M` or `F`)
1. Have a look at the beautiful `.html` maps

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

Call with `python3 cooccurrence_per_code_range.py` from `task2` directory.

Result:

```shell
001–139: infectious and parasitic diseases
    110.1 and 110.4 appearing together 2 times.
140–239: neoplasms
    216.9 and 238.2 appearing together 1 times.
240–279: endocrine, nutritional and metabolic diseases, and immunity disorders
    268.9 and 272.2 appearing together 29 times.
280–289: diseases of the blood and blood-forming organs
    280 and 281.1 appearing together 4 times.
290–319: mental disorders
    300.02 and 305.90 appearing together 20 times.
320–389: diseases of the nervous system and sense organs
    380.10 and 380.4 appearing together 8 times.
390–459: diseases of the circulatory system
    401.9 and 427.31 appearing together 9 times.
460–519: diseases of the respiratory system
    461.9 and 466.0 appearing together 38 times.
520–579: diseases of the digestive system
    530.81 and 553.3 appearing together 6 times.
580–629: diseases of the genitourinary system
    626.0 and 626.4 appearing together 6 times.
630–679: complications of pregnancy, childbirth, and the puerperium
    642.33 and 643.03 appearing together 1 times.
680–709: diseases of the skin and subcutaneous tissue
    690.10 and 691.8 appearing together 5 times.
710–739: diseases of the musculoskeletal system and connective tissue
    723.1 and 724.2 appearing together 23 times.
780–799: symptoms, signs, and ill-defined conditions
    786.05 and 786.07 appearing together 16 times.
800–999: injury and poisoning
    825.0 and 928.20 appearing together 12 times.
E: external causes of injury
    E884 and E884.9 appearing together 2 times.
V: supplemental classification
    V04.81 and V70.0 appearing together 31 times.
```

## Task 3

> Working on aggregated data:
>
> - Calculate the doctor visits per age group (0-9, 10-19, etc.) and visualize the data points. Further, use an interpolation method to estimate the doctor visits for each age. Compare the interpolated data with the actual data and calculate the mean squared error (MSE) & visualize.
>
> Model the blood pressure using linear regression:
> - Use the explanatory variables: smoking status, BMI, age (, and ...)
> - Determine the coefficient of determination R 2 for your regression.

TODO