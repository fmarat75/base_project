import streamlit as st
import pandas as pd
import numpy as np
from main.main_file import get_titanic


st.markdown("""# Page A """)

my_df = get_titanic()

st.dataframe(my_df)
