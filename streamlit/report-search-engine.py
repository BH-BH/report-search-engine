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
text_search = st.text_input("Search reports by collection, title, description or keywords", value="")

# If text_search is empty, show all reports
if text_search == "":
    df_search = df
else:
    # Convert the search text to lower case
    text_search_lower = text_search.lower()

    # Convert the DataFrame columns to lower case before applying the filter
    m1 = df["Title"].str.lower().str.contains(text_search_lower)
    m2 = df["Description"].str.lower().str.contains(text_search_lower)
    m3 = df["Collection"].str.lower().str.contains(text_search_lower)
    m4 = df["Keywords"].str.lower().str.contains(text_search_lower)
    df_search = df[m1 | m2 | m3 | m4]

# Show the results, as cards
N_cards_per_row = 3
for n_row, row in df_search.reset_index().iterrows():
    i = n_row % N_cards_per_row
    if i == 0:
        st.write("---")
        cols = st.columns(N_cards_per_row, gap="large")
    # draw the card
    with cols[n_row % N_cards_per_row]:
        st.caption(f"{row['Collection'].strip()} - {row['Type'].strip()} ")
        st.markdown(f"**{row['Title'].strip()}**")
        st.markdown(f"*{row['Description'].strip()}*")
        st.caption(f"**Last Edited:** {row['Last Edited'].strip()}")
        st.caption(f"**Last Successful Run:** {row['Last Successful Run'].strip()}")
        st.markdown(f"**{row['Link']}**")
