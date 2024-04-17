import pandas as pd
import numpy as np
import os
import requests
import base64
from PIL import Image
import io
from params import *
import math

def get_df():

    df = pd.DataFrame({
        'first column': list(range(1, 11)),
        'second column': np.arange(10, 101, 10)
    })

    return df



def get_titanic():

    parent_dir = os.getcwd()
    filepath = os.path.join(parent_dir,'raw_data', "ML_Titanic_dataset.csv")
    titanic_df = pd.read_csv(filepath)

    return titanic_df


# Function to download the satellite image
def download_satellite_image(api_key, latitude, longitude, zoom=21, size='600x600'):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={size}&maptype=satellite&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download image: {response.status_code}")


# Function to count trees via local API
def count_trees(Lat, Long, step):

    url = f"http://127.0.0.1:8000/counttrees?lat={Lat}&long={Long}&step={step}&api_key={GOOGLE_MAPS_KEY}" #### to be changed to website URL
    ##url = f"https://baseprojectapi-jf3na7mc5a-ew.a.run.app/counttrees?lat={Lat}&long={Long}&step={step}&api_key={GOOGLE_MAPS_KEY}" #### to be changed to website URL
    response = requests.get(url)

    if response.status_code == 200:

        all_response = response.json()
        trees_df = pd.read_json(all_response["trees"], orient='records')

        base64_string = all_response["image"]
        img_data = base64.b64decode(base64_string)
        tree_img = Image.open(io.BytesIO(img_data))

        return trees_df, tree_img
    else:
        raise Exception(f"Failed to count trees : {response.status_code}")


def geocode(address):
    params = { "q": address, 'format': 'json' }
    places = requests.get(f"https://nominatim.openstreetmap.org/search", params=params).json()

    first_place = places[0]
    longitude = float(first_place["lon"])
    latitude = float(first_place["lat"])
    full_address = first_place["display_name"]

    return full_address, latitude, longitude
