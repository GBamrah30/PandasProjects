import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import os

#Set title, layout and description of the webpage
st.set_page_config(page_title="Analysis of Heart Attack", layout = "wide")
st.title("📈 Heart Attack Analysis")
st.markdown("The heart attack datasets were collected at Zheen hospital in Erbil, Iraq, from January 2019 to May 2019. The below is an analysis of the data provided.")

#load data
df_path = os.path.join(os.path.dirname(__file__), "Medicaldataset.csv")
df = pd.read_csv(df_path)

#Set sidebar and sidebar filters
st.sidebar.header("Filter Patient Data")

min_age = int(df['Age'].min())
max_age = int(df['Age'].max())

start_age, end_age = st.sidebar.slider(
    "Select age range:",
    value=(min_age, max_age),
    min_value=min_age,
    max_value=max_age
)

gender_selection = st.sidebar.multiselect(
    "Select Gender(s):",
    options=["Male", "Female"],
    default=["Male", "Female"]
)

result_selection = st.sidebar.multiselect(
    "Select Diagnosis Result:",
    options=df['Result'].unique(),
    default=df['Result'].unique()
)

filtered_df = df[
    (df['Age'] >= start_age) & (df['Age'] <= end_age) &
    (df['Result'].isin(result_selection))
]

if gender_selection:
    # Map "Male" to 1 and "Female" to 0
    gender_map = {"Male": 1, "Female": 0}
    gender_values = [gender_map[g] for g in gender_selection]
    
    # Filter the already filtered_df
    filtered_df = filtered_df[filtered_df['Gender'].isin(gender_values)]

#Show dataset    
filtered_df['Gender'] = filtered_df['Gender'].map({1: "Male", 0: "Female"})
tab1, tab2 = st.tabs(["Data Set", "Metrics"])

with tab1:
    st.subheader("Market Trends and Salary")
    st.dataframe(filtered_df)
    
with tab2:
    st.subheader("Data Metrics")
    st.dataframe(filtered_df.describe())

#Histogram/KDE of age distribution and maybe heartrate distribution
st.subheader("Data Visuals")
fig1 = px.histogram(
    filtered_df,
    x='Age',
    title="Age Distribution",
    labels={'Age': 'Age'},
    color_discrete_sequence=['goldenrod']
)
st.plotly_chart(fig1)

#2x1
col1, col2 = st.columns(2)

#Scatter plot Age vs Heart Rate 
with col1:
    fig2 = px.scatter(
        filtered_df,
        x='Age',
        y='Heart rate',
        title="Age vs Heart Rate",
        labels={'Age': 'Age', 'Heart rate': 'Heart Rate'}
    )
    st.plotly_chart(fig2, use_container_width=True)

#Boxplot of heartrate by gender
with col2:
    fig3 = px.box(
        filtered_df,
        x='Gender',
        y='Heart rate',
        labels={'Gender': 'Gender', 'Heart rate': 'Heart Rate'},
        color='Gender',
        title="Heart Rate Levels by Gender"
    )
    st.plotly_chart(fig3, use_container_width=True)

#Bar chart average troponin levels by result
col3, col4 = st.columns(2)
with col3:
    average_troponin = filtered_df.groupby("Result")["Troponin"]\
        .mean().sort_values(ascending=False).reset_index()
    fig4 = px.bar(
        average_troponin,
        x='Result',
        y='Troponin',
        color='Result',
        color_discrete_map={
            'positive': "#D83220",  # Red
            'negative': "#127DC4"   # Blue
        },
        labels={'Troponin':'Troponin', 'Result':'Result'},
        title="Average Troponin Level per Diagnosis Result"
    )
    st.plotly_chart(fig4, use_container_width=True)

#Count of cases by gender
with col4:
    count_gender = filtered_df['Gender'].value_counts().reset_index()
    count_gender.columns = ['Gender', 'Count']
    fig5 = px.bar(
        count_gender,
        x = 'Count',
        y = 'Gender',
        orientation = 'h',
        color = 'Gender',
        color_discrete_map={
            'Male': "#c67440",
            'Female': "#7c2fdf"
        },
        title = "Number of Cases by Gender",
    )
    st.plotly_chart(fig5, use_container_width=True)

# Boxplot of Troponin levels across Result groups
with st.expander("Troponin Levels by Diagnosis Result"):
    fig6 = px.box(
        filtered_df,
        x='Result',
        y='Troponin',
        color='Result',
        color_discrete_map={
            'positive': "#D83220",  # Red
            'negative': "#127DC4"   # Blue
        },
        labels={'Result': 'Diagnosis Result', 'Troponin': 'Troponin Level'},
        title="Troponin Levels by Diagnosis Result"
    )
    st.plotly_chart(fig6, use_container_width=True)

# Scatter plot CK-MB vs Troponin colored by Result
with st.expander("CK-MB vs Troponin by Diagnosis Result"):
    fig7 = px.scatter(
        filtered_df,
        x='CK-MB',
        y='Troponin',
        color='Result',
        color_discrete_map={
            'positive': "#D83220",
            'negative': "#127DC4"
        },
        labels={'CK-MB': 'CK-MB Level', 'Troponin': 'Troponin Level', 'Result': 'Diagnosis Result'},
        title="Scatter Plot of CK-MB vs Troponin by Diagnosis Result",
        hover_data=['Age', 'Gender', 'Heart rate']
    )
    st.plotly_chart(fig7, use_container_width=True)

# Pie chart showing distribution of Gender within each Result category
st.subheader("Gender Distribution within Diagnosis Result Categories")
col5, col6 = st.columns(2)

with col5:
    # Pie chart for positive results gender distribution
    positive_df = filtered_df[filtered_df['Result'] == 'positive']
    pos_gender_counts = positive_df['Gender'].value_counts().reset_index()
    pos_gender_counts.columns = ['Gender', 'Count']
    fig8 = px.pie(
        pos_gender_counts,
        names='Gender',
        values='Count',
        color='Gender',
        color_discrete_map={'Male': "#c67440", 'Female': "#7c2fdf"},
        title="Gender Distribution for Positive Diagnosis",
        hole=0.4
    )
    st.plotly_chart(fig8, use_container_width=True)

with col6:
    # Pie chart for negative results gender distribution
    negative_df = filtered_df[filtered_df['Result'] == 'negative']
    neg_gender_counts = negative_df['Gender'].value_counts().reset_index()
    neg_gender_counts.columns = ['Gender', 'Count']
    fig9 = px.pie(
        neg_gender_counts,
        names='Gender',
        values='Count',
        color='Gender',
        color_discrete_map={'Male': "#c67440", 'Female': "#7c2fdf"},
        title="Gender Distribution for Negative Diagnosis",
        hole=0.4
    )
    st.plotly_chart(fig9, use_container_width=True)
    
    
st.markdown("---")
st.header("Summary & Notes")
st.markdown("""
- Dataset from Zheen Hospital (Jan-May 2019).
- This dashboard is for exploratory purposes and not medical advice.
- Troponin and CK-MB levels are important markers observed.
""")


csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_heart_data.csv',
    mime='text/csv'
)