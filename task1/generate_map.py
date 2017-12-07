"""Generated Folium/Leaflet maps with us healthcare data."""

import json
import os
import sys

import folium
import pandas as pd
import pyhdb

from bmi import BMI
from doctorvisits import DoctorVisits
from patients import Patients

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

    gender = sys.argv[1] if len(sys.argv) > 1 else None
    start_year = sys.argv[2] if len(sys.argv) > 2 else None
    end_year = sys.argv[3] if len(sys.argv) > 3 else None

    for class_var in [BMI, DoctorVisits, Patients]:
        print("Generating map: " + class_var.__name__)
        generate_map(class_var, connection, gender, start_year, end_year)

    connection.close()

def generate_map(class_var, db_conn, gender, start_year, end_year):
    """Generate map for a single module."""
    gen = class_var(db_conn)
    data = gen.generate(gender, start_year, end_year)
    state_data = pd.DataFrame(data=data, columns=["State", gen.column_name])

    fmap = folium.Map(location=[48, -102], zoom_start=3)
    fmap.choropleth(
        geo_data=STATE_GEO,
        name='choropleth',
        data=state_data,
        columns=['State', gen.column_name],
        key_on='feature.id',
        fill_color='OrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=gen.legend_name)

    folium.LayerControl().add_to(fmap)
    fmap.save(class_var.__name__ + '.html')

main()
