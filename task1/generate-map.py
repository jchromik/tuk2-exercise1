import folium
import json
import os
import pandas as pd
import pyhdb

from task1.patients import Patients

with open("../db-conf.json") as db_conf_file:
  db_conf = json.load(db_conf_file)

#pdb.set_trace()

connection = pyhdb.connect(
  host=db_conf["host"],
  port=db_conf["port"],
  user=db_conf["user"],
  password=db_conf["password"],
)

# gen = doctorvisits.DoctorVisits(connection)
# data = gen.generate()

gen = Patients(connection)
data = gen.generate()

connection.close()

state_data = pd.DataFrame(data=data, columns=["State", gen.column_name])
state_geo = os.path.join('.', 'resources/us-states.json')

m = folium.Map(location=[48, -102], zoom_start=3)

m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', gen.column_name],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=gen.legend_name
)

folium.LayerControl().add_to(m)

m.save('map.html')
