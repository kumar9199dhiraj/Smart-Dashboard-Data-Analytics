import streamlit as  st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Smart Dashboard Data Analytics")

file= st.file_uploader(" upload csv file")
if file:
    df = pd.read_csv(file)

    st.subheader(" Data Preview")
    st.dataframe(df.head(10))

    numeric_columns=df.select_dtypes(include='number').columns.tolist()

    st.sidebar.header(" Controls")

    chart_type=st.sidebar.selectbox(
        "Select Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart","Hist Chart"]
    )

    x_cols = st.sidebar.selectbox("Select X-axis", df.columns)
    if numeric_columns:
        y_cols = st.sidebar.selectbox("Select Y-axis", numeric_columns)

        st.subheader("Visualization")
        if chart_type == "Bar Chart":
            st.bar_chart(df[[x_cols, y_cols]].set_index(x_cols))

        elif chart_type == "Line Chart":
            st.line_chart(df[[x_cols, y_cols]].set_index(x_cols))

        elif chart_type == "Pie Chart":
            pie_data = df.groupby(x_cols)[y_cols].sum()
            fig, ax= plt.subplots(figsize=(5,6))
            ax.pie(
                pie_data,
                labels=pie_data.index,
                autopct="%1.1f%%",
                startangle=90,
                pctdistance=0.8,
                radius=0.3,
            )
            ax.axis("equal")
            st.pyplot(fig)

        elif chart_type == "Hist Chart":
            fig,ax = plt.subplots(figsize=(7,4))
            ax.hist(df[y_cols], bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribution of {y_cols}")
            ax.set_xlabel(y_cols)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

        st.subheader("statistics")
        st.write(df[y_cols].describe())

    else:
        st.warning("No numeric columns found in data ")
