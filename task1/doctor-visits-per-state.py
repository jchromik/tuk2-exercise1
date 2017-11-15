import folium
import json
import os
import pandas as pd
import pyhdb

db_conf_file = open("../db-conf.json")
db_conf = json.load(db_conf_file)

connection = pyhdb.connect(
    host=db_conf["host"],
    port=db_conf["port"],
    user=db_conf["user"],
    password=db_conf["password"]
)

db_conf_file.close()

cursor = connection.cursor()
cursor.execute("""
DROP VIEW "TUKGRP7"."Visits"
""")
cursor.execute("""
CREATE VIEW "Visits" AS (
  SELECT "PatientGuid", COUNT("TranscriptGuid") AS "Visits"
  FROM "TUKGRP7"."Transcript"
  GROUP BY "PatientGuid")
""")
cursor.execute("""
SELECT "State", AVG("Visits")
FROM "TUKGRP7"."Visits", "TUKGRP7"."Patient"
WHERE "TUKGRP7"."Visits"."PatientGuid" = "TUKGRP7"."Patient"."PatientGuid"
GROUP BY "State"
""")

visits = cursor.fetchall()
connection.close()

visits = list(map(lambda tuple : (tuple[0], float(tuple[1])), visits))
state_data = pd.DataFrame(data=visits, columns=["State", "Visits"])

state_geo = os.path.join('.', 'us-states.json')

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'Visits'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Average Visits'
)

folium.LayerControl().add_to(m)

m.save('doctor-visits-per-state.html')
