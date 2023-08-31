# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Report Search Engine", page_icon="🐍", layout="wide")
st.title("Report Search Engine")

# Connect to the Google Sheet
sheet_id = "1_EwcotTbMxPEYhhN432miTFleYquDTj8cAR11zmIEl4"
sheet_name = "Reports"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

# Show the dataframe (we'll delete this later)
st.write(df)