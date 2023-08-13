import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a title
st.title("Visualização de dados com streamlit")

# Upload CSV file
uploaded_file = st.file_uploader("Envie seu CSV", type=["csv"])

# Visualização baseada na opção selecionada
if uploaded_file is not None:
    df_temp = pd.read_csv(uploaded_file)
    
    # Display the loaded DataFrame
    st.subheader("DataFrame")
    st.write(df_temp.head())

    visualization_option = st.sidebar.selectbox("Selecione Visualização", ["Correlation Heatmap", "Histograms", "Box Plots", "Scatter Plot"])

 

    elif visualization_option == "Histograms":
        st.subheader("Histograms")
        for column in df_temp.columns:
            st.write(f"{column} distribution")
            fig = plt.figure()
            df_temp[column].hist(bins=20, ax=fig.gca())
            st.pyplot(fig)

    elif visualization_option == "Box Plots":
        st.subheader("Box Plots")
        x_column = st.selectbox("Select X-axis Column", df_temp.columns)
        y_column = st.selectbox("Select Y-axis Column", df_temp.columns)
        fig, ax = plt.subplots()
        sns.boxplot(x=x_column, y=y_column, data=df_temp, ax=ax)
        st.pyplot(fig)

    elif visualization_option == "Scatter Plot":
        st.subheader("Scatter Plot")
        x_column = st.selectbox("Select X-axis Column", df_temp.columns)
        y_column = st.selectbox("Select Y-axis Column", df_temp.columns)
        fig, ax = plt.subplots()
        ax.scatter(df_temp[x_column], df_temp[y_column])
        st.pyplot(fig)

    # Add a button to reload the data
    st.button("Recarregar Csv")
