import pandas as pd
import streamlit as st

# Set the title for the Streamlit app
st.title('GATE Score Extractor - Classified Data')

# Read the classified data from the CSV file
df = pd.read_csv('classified_text.csv')

# Display the dataframe in a table format
st.subheader('Extracted and Classified Data:')
st.dataframe(df)  # Streamlit's method to display dataframes

# Optional: Display specific columns or allow filtering
# You could create interactive filters or widgets here