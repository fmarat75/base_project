import streamlit as st
import numpy as np
import pandas as pd
from main.main_file import get_df


st.markdown("""# Base Project
## Welcome
See below results""")

my_df = get_df()

st.dataframe(my_df)
