SELECT D1."DiagnosisDescription", D2."DiagnosisDescription", COUNT(*) AS "Occurrence"
FROM
	"TUKGRP7"."Diagnosis" AS D1 INNER JOIN "TUKGRP7"."Diagnosis" AS D2
	ON  D1."PatientGuid" = D2."PatientGuid"
	AND D1."StartYear" = D2."StartYear"
	AND D1."DiagnosisDescription" < D2."DiagnosisDescription"
GROUP BY D1."DiagnosisDescription", D2."DiagnosisDescription"
ORDER BY "Occurrence" DESC
LIMIT 10

/* server processing time: 66 ms 340 µs */