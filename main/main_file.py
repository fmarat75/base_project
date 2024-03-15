import pandas as pd
import numpy as np
import os
import requests

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
def download_satellite_image(api_key, latitude, longitude, zoom=12, size='600x600'):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitude},{longitude}&zoom={zoom}&size={size}&maptype=satellite&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download image: {response.status_code}")
