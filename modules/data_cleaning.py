import streamlit as st
import pandas as pd

def clean_data(df):
    st.subheader("🧹 Data Cleaning Options")

    temp_df = df.copy()  # Use a temporary copy for preview and changes

    st.write(f"Initial dataset shape: {df.shape}")

    # Dropping unnecessary columns
    st.subheader("Drop Unncessary Columns")
    drop_cols = st.multiselect("Select columns to drop", temp_df.columns.tolist())
    if drop_cols:
        temp_df = temp_df.drop(columns=drop_cols)
        st.success(f"Columns {drop_cols} dropped successfully!")

    # Handle missing values
    st.markdown("### 🔍 Handle Missing Values")
    missing_cols = temp_df.columns[temp_df.isnull().any()]

    if missing_cols.any():
        for col in missing_cols:
            option = st.selectbox(
                f"How to handle {temp_df[col].isnull().sum()} missing values in '{col}'?",
                ("Do nothing", "Drop rows", "Fill with mean", "Fill with median", "Fill with mode","Fill with custom value"),
                key=f"missing_{col}"
            )
            if option == "Drop rows":
                temp_df = temp_df.dropna(subset=[col])
            elif option == "Fill with mean":
                temp_df[col] = temp_df[col].fillna(temp_df[col].mean())
            elif option == "Fill with median":
                temp_df[col] = temp_df[col].fillna(temp_df[col].median())
            elif option == "Fill with mode":
                temp_df[col] = temp_df[col].fillna(temp_df[col].mode()[0])
            elif option == "Fill with custom value":
                custom_value = st.text_input(f"Enter custom value for '{col}")
                if custom_value:
                    temp_df[col] = temp_df[col].fillna(custom_value)

    else:
        st.success("No missing values in the dataset ✅")

    # Remove duplicates
    st.markdown("### 🧽 Remove Duplicate Rows")
    st.write(temp_df.duplicated().sum(), "duplicate rows found.")
    if st.checkbox("Remove duplicate rows"):
        initial = temp_df.shape[0]
        temp_df = temp_df.drop_duplicates()
        st.info(f"{initial - temp_df.shape[0]} duplicate rows removed.")

    # Convert data types
    st.markdown("### 🔄 Convert Data Types (Optional)")
    for col in temp_df.select_dtypes(include=['object']).columns:
        if st.checkbox(f"Convert '{col}' to category", key=f"cat_{col}"):
            temp_df[col] = temp_df[col].astype('category')
        if pd.to_numeric(temp_df[col], errors='coerce').notnull().any():
            if st.checkbox(f"Convert '{col}' to numeric", key=f"num_{col}"):
                temp_df[col] = pd.to_numeric(temp_df[col], errors='coerce')

    st.markdown("### 👀 Preview of Under Cleaning Data")
    st.dataframe(temp_df)
    st.write(f"Cleaned dataset shape: {temp_df.shape}")

    # Save button
    if st.button("✅ Save Cleaned Data"):
        st.session_state['cleaned_df'] = temp_df
        st.success("Cleaned data saved successfully!")
    else:
        st.info("🔄 This is only a preview. Click 'Save Cleaned Data' to apply changes.")

    return st.session_state.get('cleaned_df', df)  # Use cleaned data if saved
