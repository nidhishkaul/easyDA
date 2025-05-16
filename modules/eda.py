import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda(df):
    st.subheader("📈 Exploratory Data Analysis")

    st.markdown("### 🔢 Dataset Summary")
    st.write(df.describe())

    st.markdown("### 🧮 Data Types & Null Values")
    st.write(df.dtypes)
    st.write(df.isnull().sum())

    st.markdown("### 📊 Value Counts (Categorical Columns)")
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    for col in cat_cols:
        if st.checkbox(f"Show value counts for '{col}'"):
            st.write(df[col].value_counts())

    st.markdown("### 🔗 Correlation Heatmap")
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(num_cols) >= 2:
        fig, ax = plt.subplots()
        sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Not enough numerical columns for a correlation heatmap.")

    st.markdown("### 🧭 Distribution Plot")
    selected_col = st.selectbox("Select a numerical column to view distribution", num_cols)
    if selected_col:
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax)
        st.pyplot(fig)

    st.markdown("### Pair Plot")
    if len(num_cols) >= 2:
        fig = sns.pairplot(df[num_cols])
        st.pyplot(fig)
    else:
        st.warning("Not enough numerical columns for a pair plot.")