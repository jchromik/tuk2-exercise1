"""Generated Folium/Leaflet maps with us healthcare data."""

import json
import os

import folium
import pandas as pd
import pyhdb

from patients import Patients
from doctorvisits import DoctorVisits

STATE_GEO = os.path.join('.', 'resources/us-states.json')

def main():
    """Generate map for data from each module."""
    with open("../db-conf.json") as db_conf_file:
        db_conf = json.load(db_conf_file)

    connection = pyhdb.connect(
        host=db_conf["host"],
        port=db_conf["port"],
        user=db_conf["user"],
        password=db_conf["password"],
    )

    for class_var in [DoctorVisits, Patients]:
        generate_map(class_var, connection)

    connection.close()

def generate_map(class_var, db_conn):
    """Generate map for a single module."""
    gen = class_var(db_conn)
    data = gen.generate()
    state_data = pd.DataFrame(data=data, columns=["State", gen.column_name])

    fmap = folium.Map(location=[48, -102], zoom_start=3)
    fmap.choropleth(
        geo_data=STATE_GEO,
        name='choropleth',
        data=state_data,
        columns=['State', gen.column_name],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=gen.legend_name)

    folium.LayerControl().add_to(fmap)
    fmap.save(class_var.__name__ + '.html')

main()
