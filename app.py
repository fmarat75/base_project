import streamlit as st
import pandas as pd
from params import *
from main.main_file import count_trees, geocode
from streamlit_fct import set_background
import time

set_background("background.png")

st.markdown("""# Neighborhood TreeVision""")
st.markdown(" ")  # Adds a space
st.markdown(""" Count the trees of your neighborhood via satellite images  """)
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Ask User for Address
base_address = st.text_input('Pick up address', '')

# Check if the user has input an address
if base_address:
    # Run geocode function only if there is an address input
    full_address, Lat, Long = geocode(base_address)
    st.markdown("The address detected is:")
    st.markdown(f"{full_address}")
else:
    st.markdown("*Example: 120 Avenue de Suffren, 75015, Paris, France*")

st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space
area_df = pd.DataFrame({
    'area': ["75m x 75m", "150m x 150m", "225m x 225m"],
    'step': [0, 1, 2],
    'time': ["50 seconds", "8 minutes", "13 minutes"]
    })
option = st.selectbox('Select size area', area_df['area'])
step = area_df[area_df['area']==option]['step'].iloc[0]
time_estim = area_df[area_df['area']==option]['time'].iloc[0]
st.markdown(f"*Estimated time to compute: {time_estim}*")
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space


resultsbtn = st.button('Count Trees')
if resultsbtn:
    with st.spinner("Counting trees..."):
        progress_bar = st.progress(0)
        total_time = {'50 seconds': 50, '8 minutes': 450, '13 minutes': 800}[time_estim]
        #total_time = 20
        for i in range(total_time):
            time.sleep(1)  # Sleep for a second
            progress_bar.progress((i + 1) / total_time)
        trees_df, tree_img = count_trees(Lat, Long, step)

    st.markdown(f"There are {len(trees_df)} trees estimated in this image")
    st.image(tree_img, caption='Satellite Image', use_column_width=True)
