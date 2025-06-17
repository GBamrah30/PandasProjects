#Imports and Setup
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Set title, layout and a description of the page
st.set_page_config(page_title = "Global AI Market Trends & Salary 2025", layout = "wide")
st.title("📊Global AI Market Trends & Salary 2025")
st.markdown("The below dataset provides an extensive analysis of the artificial intelligence job market with over 15,000 real job postings collected from major job platforms worldwide. \n\nIt includes detailed salary information, job requirements, company insights, and geographic trends.")\
    
#Load data set
df = pd.read_csv("ai_job_dataset.csv")

#Convert to proper datetime format
df['posting_date'] = pd.to_datetime(df['posting_date'], errors='coerce')

#Side bar header
st.sidebar.header("Data Filters")

#Get columns I want to filter
df = df.dropna(subset=['posting_date'])

min_date = df['posting_date'].min().date()
max_date = df['posting_date'].max().date()

start_date, end_date = st.sidebar.date_input(
    "Select posting date range:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

df = df.dropna(subset=['years_experience'])

min_exp = int(df['years_experience'].min())
max_exp = int(df['years_experience'].max())

experience_range = st.sidebar.slider(
    "Select range of required experience (years):",
    min_value=min_exp,
    max_value=max_exp,
    value=(min_exp, max_exp)  # default range is full range
)

selected_country = st.sidebar.multiselect("Select Country", options=df['company_location'].unique(), default=df['company_location'].unique())
selected_title = st.sidebar.multiselect("Select Job Title", options=df['job_title'].unique(), default=df['job_title'].unique())

filtered_df = df[
    (df['posting_date'].dt.date >= start_date) & (df['posting_date'].dt.date <= end_date) &
    (df['years_experience'] >= experience_range[0]) & (df['years_experience'] <= experience_range[1]) &
    (df['company_location'].isin(selected_country)) &
    (df['job_title'].isin(selected_title))
]

#Show table of dataset
st.subheader("Market Trends and Salary")
st.dataframe(filtered_df)

# Average salary by country
st.subheader("Average Salary by Country")
country_salary = filtered_df.groupby("employee_residence")["salary_usd"]\
    .mean().sort_values(ascending=False).reset_index()
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x="salary_usd", y="employee_residence", data=country_salary, ax=ax1)
ax1.set_title("Average Salary by Country")
ax1.set_xlabel("Average Salary (USD)")
ax1.set_ylabel("Country")
st.pyplot(fig1)

# Salary distribution by experience level
st.subheader("Salary Distribution by Experience Level")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='experience_level', y='salary_usd', data=filtered_df, ax=ax2)
ax2.set_title("Salary Distribution by Experience Level")
ax2.set_xlabel("Experience Level")
ax2.set_ylabel("Salary (USD)")
st.pyplot(fig2)

# Job count by role
st.subheader("Most Common Job Titles")
top_titles = filtered_df['job_title'].value_counts().nlargest(10).reset_index()
top_titles.columns = ['Job Title', 'Count']
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x="Count", y="Job Title", data=top_titles, ax=ax3)
ax3.set_title("Top 10 Most Common Job Titles")
st.pyplot(fig3)

# Company size vs average salary
st.subheader("Company Size vs Average Salary")
size_salary = filtered_df.groupby('company_size')["salary_usd"].mean().reset_index()
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.barplot(x='company_size', y='salary_usd', data=size_salary, ax=ax4)
ax4.set_title("Company Size vs Average Salary")
ax4.set_xlabel("Company Size")
ax4.set_ylabel("Average Salary (USD)")
st.pyplot(fig4)

# Salary trend by year if available
if 'year' in df.columns and df['year'].notna().any():
    st.subheader("Salary Trend Over Time")
    year_salary = filtered_df.groupby('year')["salary_usd"].mean().reset_index()
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='year', y='salary_usd', data=year_salary, marker="o", ax=ax5)
    ax5.set_title("Average Salary Over Time")
    ax5.set_xlabel("Year")
    ax5.set_ylabel("Average Salary (USD)")
    st.pyplot(fig5)

# Summary statistics
st.subheader("Salary Summary Statistics")
st.write(filtered_df['salary_usd'].describe())

# Download filtered data
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(filtered_df)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_ai_jobs.csv',
    mime='text/csv',
)