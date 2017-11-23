import folium
import json
import os
import pandas as pd
import pyhdb

import doctorvisits

with open("../db-conf.json") as db_conf_file:
  db_conf = json.load(db_conf_file)

connection = pyhdb.connect(
  host=db_conf["host"],
  port=db_conf["port"],
  user=db_conf["user"],
  password=db_conf["password"]
)

dv = doctorvisits.DoctorVisits(connection)
visits = dv.generate()

connection.close()

state_data = pd.DataFrame(data=visits, columns=["State", dv.column_name])
state_geo = os.path.join('.', 'us-states.json')

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', dv.column_name],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=dv.legend_name
)

folium.LayerControl().add_to(m)

m.save('map.html')
