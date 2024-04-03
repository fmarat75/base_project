import streamlit as st
import pandas as pd
from params import *
from main.main_file import count_trees


st.markdown("""# Count Trees """)
st.markdown(" ")  # Adds a space
st.markdown(" ")  # Adds a space

# Ask User for Lat/Long
Lat = st.number_input(label="Enter your latitude", value=40.4248077, format="%.7f")
Long = st.number_input(label="Enter your longitude", value=-3.6938166, format="%.7f")

resultsbtn = st.button('Count Trees')
if resultsbtn:

    trees_df, tree_img = count_trees(Lat, Long)

    st.markdown(f"There are {len(trees_df)} tree(s) in this image")
    st.image(tree_img, caption='Satellite Imag', use_column_width=True)
    st.dataframe(trees_df)
