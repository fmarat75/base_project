import streamlit as st
from params import *
from main import download_satellite_image


st.markdown("""# Satellite Image Downloader """)


api_key = GOOGLE_MAPS_KEY
latitude = 48.8566  # Latitude for Paris
longitude = 2.3522  # Longitude for Paris

if st.button('Download Image'):
    try:
        image_data = download_satellite_image(api_key, latitude, longitude)
        st.image(image_data, caption='Satellite Image of Paris', use_column_width=True)
    except Exception as e:
        st.error(f"Error: {e}")
