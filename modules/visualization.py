import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_visuals(df):
    st.subheader("📊 Data Visualization")

    st.markdown("### 📌 Select Plot Type")
    plot_type = st.selectbox("Choose a plot type", ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot", "Box Plot"])

    all_columns = df.columns.tolist()
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()

    if plot_type == "Bar Chart":
        group_by = st.checkbox("Use Group By", value=False)
        if group_by:
            group_by_col = st.selectbox("Group by (Categorical)", categorical_columns, key="group_by_col")
            agg_col = st.selectbox("Aggregate by (Numeric)", numeric_columns, key="agg_col")
            agg_func = st.selectbox("Aggregation Function", ["mean", "sum", "count"], key="agg_func")
            if st.button("Generate Bar Chart with Group By"):
                if agg_func == "mean":
                    grouped_df = df.groupby(group_by_col)[agg_col].mean().reset_index()
                elif agg_func == "sum":
                    grouped_df = df.groupby(group_by_col)[agg_col].sum().reset_index()
                elif agg_func == "count":
                    grouped_df = df.groupby(group_by_col)[agg_col].count().reset_index()
                st.subheader("Bar Chart")
                st.bar_chart(x=group_by_col, y=agg_col, data=grouped_df)
        else:
            x_col = st.selectbox("X-axis (Categorical)", categorical_columns)
            y_col = st.selectbox("Y-axis (Numeric)", numeric_columns)
            if st.button("Generate Bar Chart"):
                st.subheader("Bar Chart")
                st.bar_chart(x=x_col, y=y_col, data=df)

    elif plot_type == "Line Chart":
        group_by = st.checkbox("Use Group By", value=False)
        if group_by:
            group_by_col = st.selectbox("Group by (Categorical)", categorical_columns, key="group_by_col")
            agg_col = st.selectbox("Aggregate by (Numeric)", numeric_columns, key="agg_col")
            agg_func = st.selectbox("Aggregation Function", ["mean", "sum", "count"], key="agg_func")
            if st.button("Generate Line Chart with Group By"):
                if agg_func == "mean":
                    grouped_df = df.groupby(group_by_col)[agg_col].mean().reset_index()
                elif agg_func == "sum":
                    grouped_df = df.groupby(group_by_col)[agg_col].sum().reset_index()
                elif agg_func == "count":
                    grouped_df = df.groupby(group_by_col)[agg_col].count().reset_index()
                st.subheader("Line Chart")
                st.line_chart(x=group_by_col, y=agg_col, data=grouped_df) 

        else:
            x_col = st.selectbox("X-axis (Categorical)", categorical_columns)
            y_col = st.selectbox("Y-axis (Numeric)", numeric_columns)
            if st.button("Generate Line Chart"):
                st.subheader("Line Chart")
                st.line_chart(x=x_col, y=y_col, data=df)

    elif plot_type == "Pie Chart":
        group_by = st.checkbox("Use Group By", value=False)
        if group_by:
            group_by_col = st.selectbox("Group by (Categorical)", categorical_columns, key="group_by_col")
            agg_col = st.selectbox("Aggregate by (Numeric)", numeric_columns, key="agg_col")
            agg_func = st.selectbox("Aggregation Function", ["mean", "sum", "count"], key="agg_func")
            if st.button("Generate Pie Chart with Group By"):
                if agg_func == "mean":
                    grouped_df = df.groupby(group_by_col)[agg_col].mean().reset_index()
                elif agg_func == "sum":
                    grouped_df = df.groupby(group_by_col)[agg_col].sum().reset_index()
                elif agg_func == "count":
                    grouped_df = df.groupby(group_by_col)[agg_col].count().reset_index()
                fig, ax = plt.subplots()
                st.subheader("Pie Chart")
                ax.pie(grouped_df[agg_col], labels=grouped_df[group_by_col], autopct='%1.1f%%')
                ax.set_ylabel("")
                st.pyplot(fig)
        else:
            col = st.selectbox("Select a categorical column", categorical_columns)
            if st.button("Generate Pie Chart"):
                fig, ax = plt.subplots()
                st.subheader("Pie Chart")
                df[col].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
                ax.set_ylabel("")
                st.pyplot(fig)

    elif plot_type == "Scatter Plot":
        x_col = st.selectbox("X-axis", numeric_columns, key="scatter_x")
        y_col = st.selectbox("Y-axis", numeric_columns, key="scatter_y")
        hue_col = st.selectbox("Color by (Optional)", [None] + categorical_columns)
        if st.button("Generate Scatter Plot"):
            st.subheader("Scatter Plot")
            if hue_col:
                st.scatter_chart(x=x_col, y=y_col,data=df, color=hue_col)
            else:
                st.scatter_chart(x=x_col, y=y_col,data=df)

    elif plot_type == "Box Plot":
        y_col = st.selectbox("Select numeric column", numeric_columns, key="boxplot_y")
        x_col = st.selectbox("Group by (categorical)", categorical_columns, key="boxplot_x")
        if st.button("Generate Box Plot"):
            st.subheader("Box Plot")
            fig, ax = plt.subplots()
            sns.boxplot(x=df[x_col], y=df[y_col], ax=ax)
            plt.xticks(rotation=90)
            st.pyplot(fig)
