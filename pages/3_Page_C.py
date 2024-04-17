import streamlit as st
import pandas as pd
from params import *
from main.main_file import count_trees, geocode


st.markdown("""# Count Trees """)
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Ask User for Address
base_address = st.text_input('Pick up address', 'Calle Barbara de Braganza 30, 28004, Madrid, Spain')
full_address, Lat, Long = geocode(base_address)

area_df = pd.DataFrame({
    'area': ["75m x 75m", "150m x 150m", "225m x 225m"],
    'step': [0, 1, 2]
    })
option = st.selectbox('Select size area', area_df['area'])
step = area_df[area_df['area']==option]['step'].iloc[0]

resultsbtn = st.button('Count Trees')
if resultsbtn:

    st.markdown(" ")  # Adds a space
    st.markdown(f"The address selected is {full_address}:")
    st.markdown(f"{full_address}")
    st.markdown(" ")  # Adds a space

    trees_df, tree_img = count_trees(Lat, Long, step)

    st.markdown(f"There are {len(trees_df)} tree(s) in this image")
    st.image(tree_img, caption='Satellite Imag', use_column_width=True)
    st.dataframe(trees_df)
