import streamlit as st
import pandas as pd
import openpyxl
from modules import data_cleaning, eda, visualization, run_query

st.set_page_config(page_title="DataAnalysisMadeEasy", layout="wide")

st.title("📊 EasyDA")
st.subheader("Your one-stop solution for data analysis!")

st.write("Welcome to EasyDA! This app simplifies data analysis with a user-friendly interface.")
st.write("Upload your dataset, perform data cleaning, and visualize your data effortlessly.")
st.write("Select an option from the sidebar to get started.")

# Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Upload", "Data Cleaning", "EDA", "Visualization","Work with SQL"])

# File uploader
uploaded_file = st.sidebar.file_uploader(" Upload your dataset", type=['csv', 'xlsx'])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    if 'cleaned_df' in st.session_state:
        st.subheader("Preview of Cleaned Dataset")
        st.dataframe(st.session_state['cleaned_df'])
    else:
        st.subheader("Preview of Uploaded Dataset")
        st.dataframe(df)

    # Routing based on selected option
    if option == "Data Cleaning":
        st.header("🧹 Data Cleaning ")
        df = data_cleaning.clean_data(df)
    elif option == "EDA":
        if 'cleaned_df' in st.session_state:
            eda.run_eda(st.session_state['cleaned_df'])
        else:
            eda.run_eda(df)
    elif option == "Work with SQL":
        st.subheader("🧮 SQL Query")
        if 'cleaned_df' in st.session_state:
            run_query.run_query(st.session_state['cleaned_df'])
        else:
            run_query.run_query(df)
    elif option == "Visualization":
        if 'cleaned_df' in st.session_state:
            visualization.plot_visuals(st.session_state['cleaned_df'])
        else:
            visualization.plot_visuals(df)
else:
    st.info("👈 Upload a file to begin")
