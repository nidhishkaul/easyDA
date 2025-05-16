import streamlit as st
from pandasql import sqldf

def run_query(df):
        query = st.text_area("Write your SQL query below...", placeholder="SELECT * FROM df WHERE ...")

        if st.button("Run SQL Query"):
        
            try:
                    # Use pandasql to run the SQL query
                    local_env = {'df': df}
                    result = sqldf(query, local_env)
                    st.success("Query executed successfully!")
                    st.dataframe(result)
            except Exception as e:
                    st.error(f"Error executing query: {e}")