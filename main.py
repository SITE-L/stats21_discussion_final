import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)  # Disable the warning message

web_apps = st.sidebar.selectbox("Select Web Apps", ("Exploratory Data Analysis", "Distributions"))

if web_apps == "Exploratory Data Analysis":
    uploaded_file = st.sidebar.file_uploader("Choose a file")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        show_df = st.checkbox("Show Data Frame", key="disabled")
        if show_df:
            st.write(df)

        st.sidebar.subheader("Column Analysis")
        selected_column = st.sidebar.selectbox("Select a Column", df.columns)

        column_type = df[selected_column].dtype

        if column_type == "object":
            st.subheader("Categorical Column Analysis")
            st.write("Selected Column:", selected_column)

            # Display value counts
            value_counts = df[selected_column].value_counts()
            st.write("Value Counts:")
            st.write(value_counts)

            # Generate bar plot
            plt.figure(figsize=(10, 6))
            sns.countplot(x=selected_column, data=df)
            plt.title("Bar Plot of " + selected_column)
            plt.xlabel(selected_column)
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            st.pyplot(plt.gcf())

        elif column_type in ["int64", "float64"]:
            st.subheader("Numerical Column Analysis")
            st.write("Selected Column:", selected_column)

            # Display summary statistics
            summary_stats = df[selected_column].describe()
            st.write("Summary Statistics:")
            st.write(summary_stats)

            # Generate histogram
            plt.figure(figsize=(10, 6))
            sns.histplot(df[selected_column], kde=True)
            plt.title("Histogram of " + selected_column)
            plt.xlabel(selected_column)
            plt.ylabel("Count")
            st.pyplot(plt.gcf())

else:
    st.write("Other web app options will be added in the future.")
