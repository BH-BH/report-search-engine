# Import libraries
import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="Report Search Engine", page_icon="📊", layout="wide")
st.title("Data Report Search Engine")

# Connect to the Google Sheet
sheet_id = "1_EwcotTbMxPEYhhN432miTFleYquDTj8cAR11zmIEl4"
sheet_name = "Reports"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search reports by title, description or keywords", value="")

# Filter the dataframe using masks
m1 = df["Title"].str.contains(text_search)
m2 = df["Description"].str.contains(text_search)
m3 = df["Keywords"].str.contains(text_search)
df_search = df[m1 | m2 | m3]

# Show the results, if you have a text_search
if text_search:
    st.write(df_search)