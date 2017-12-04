SELECT D1."ICD9Code", D2."ICD9Code", COUNT(*) AS "Occurrence"
FROM
	"TUKGRP7"."Diagnosis" AS D1 INNER JOIN "TUKGRP7"."Diagnosis" AS D2
	ON  D1."PatientGuid" = D2."PatientGuid"
	AND D1."StartYear" = D2."StartYear"
	AND D1."ICD9Code" < D2."ICD9Code"
GROUP BY D1."ICD9Code", D2."ICD9Code"
ORDER BY "Occurrence" DESC
LIMIT 10

/* server processing time: 58 ms 789 µs */