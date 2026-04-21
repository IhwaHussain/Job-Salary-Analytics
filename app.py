import os
import streamlit as st
import pandas as pd
import plotly.express as px

from ingestion import get_data
import model_bls

# --- App Config ---
st.set_page_config(
    page_title="Job Salary Analytics",
    page_icon="💼",
    layout="wide"
)

# --- Custom CSS ---
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] { background-color: #181828; }
        .main { background-color: #232340;}
        h1, h2, h3, h4, h5, h6 {
            color: #e2e2e2;
        }
        .stPlotlyChart { background-color: #232340 !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Data Loading ---
DATA_DIR = "data"
BLS_PATH = os.path.join(DATA_DIR, "bls_data.csv")
ILO_PATH = os.path.join(DATA_DIR, "ilo_data.csv")

@st.cache_data(show_spinner=True)
def load_all_data():
    bls_df, ilo_df = get_data(BLS_PATH, ILO_PATH)
    return bls_df, ilo_df

bls_df, ilo_df = load_all_data()

# --- Sidebar ---
st.sidebar.title("📊 Job Salary Analytics")
page = st.sidebar.radio(
    "Navigate",
    ("Data Overview", "BLS Salary Model")
)
st.sidebar.markdown("---")
st.sidebar.markdown("[GitHub Repo](https://github.com/IhwaHussain/Job-Salary-Analytics)")

# --- Utils ---
def salary_range(pred, delta=0.08):
    return int(pred * (1 - delta)), int(pred * (1 + delta))

# --- Page 1: Data Overview ---
if page == "Data Overview":
    st.title("Labor Market Data Overview")
    st.write("Explore BLS occupational employment and wage statistics.")

    with st.expander("Raw Data Preview"):
        st.write("BLS data", bls_df.head())
        if ilo_df is not None:
            st.write("ILO data", ilo_df.head())

    st.subheader("Salary Distribution by Job Title")
    job_title = st.selectbox("Pick a job title:", bls_df['Job Title'].unique())
    filtered = bls_df[bls_df['Job Title'] == job_title]
    fig = px.histogram(filtered, x="Salary", nbins=30, color="Region",
                       title=f"Salary Distribution — {job_title}")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top 10 Highest Paying Roles")
    top_roles = bls_df.groupby("Job Title")["Salary"].mean().sort_values(ascending=False).head(10)
    fig = px.bar(top_roles, orientation='h', title="Top 10 Highest Paying Roles")
    st.plotly_chart(fig, use_container_width=True)

    if 'Industry' in bls_df.columns:
        st.subheader("Highest Demand Industries")
        top_industries = bls_df['Industry'].value_counts().head(10)
        fig = px.bar(top_industries, orientation='h', title="Top 10 Highest Demand Industries")
        st.plotly_chart(fig, use_container_width=True)

    if 'Year' in bls_df.columns:
        st.subheader("Salary Trends (2023–2024)")
        trend = bls_df.groupby('Year')['Salary'].mean().reset_index()
        fig = px.line(trend, x='Year', y='Salary', markers=True)
        st.plotly_chart(fig, use_container_width=True)

# --- Page 2: BLS Salary Model ---
elif page == "BLS Salary Model":
    st.title("BLS Salary Prediction")
    st.write("Predict expected salary using job title, region, and experience level based on real BLS data.")

    col1, col2 = st.columns(2)
    with col1:
        job_title = st.selectbox("Job Title", bls_df['Job Title'].unique())
        region = st.selectbox("Region", bls_df['Region'].unique())
    with col2:
        experience = st.slider("Experience Level (years)", 0, 40, 2)

    if st.button("Predict Salary"):
        try:
            model = model_bls.load_model()
            pred = model_bls.predict_salary(job_title, region, experience, model)
            low, high = salary_range(pred)
            st.success(f"Estimated salary for '{job_title}' in {region} with {experience} yrs exp: **${low:,}–${high:,}**")
        except Exception as e:
            st.error(f"Prediction error: {e}")

    st.markdown("---")
    st.subheader("Salary by Region")
    fig = px.box(bls_df, x='Region', y='Salary', color='Region', points='all')
    st.plotly_chart(fig, use_container_width=True)



  
