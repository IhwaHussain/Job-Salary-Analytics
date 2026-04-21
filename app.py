import os
import streamlit as st
import pandas as pd
import plotly.express as px

from ingestion import get_data, generate_sample_data
import model_bls
import model_bls_li

# --- App Config (dark theme, page, favicon) ---
st.set_page_config(
    page_title="Job Salary Analytics",
    page_icon="💼",
    layout="wide"
)

# --- Custom CSS for dark professional theme ---
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] { background-color: #181828; }
        .main { background-color: #232340;}
        h1, h2, h3, h4, h5, h6, .st-bx, .st-bn {
            color: #e2e2e2;
        }
        .stPlotlyChart { background-color: #232340 !important; }
    </style>
    """,
    unsafe_allow_html=True
)

##### --- SETTINGS & DATA LOADING -----

DATA_DIR = "data"
BLS_PATH = os.path.join(DATA_DIR, "bls_data.csv")
ILO_PATH = os.path.join(DATA_DIR, "ilo_data.csv")
LI_PATH = os.path.join(DATA_DIR, "linkedin_data.csv")

@st.cache_data(show_spinner=True)
def load_all_data():
    bls_df, ilo_df = get_data(BLS_PATH, ILO_PATH)
    if os.path.exists(LI_PATH):
        li_df = pd.read_csv(LI_PATH)
    else:
        # If LinkedIn data is missing, use some sample data with industry.
        li_df = generate_sample_data()
    return bls_df, ilo_df, li_df

bls_df, ilo_df, li_df = load_all_data()

##### --- SIDEBAR NAVIGATION -----
st.sidebar.title("📊 Job Salary Analytics")
page = st.sidebar.radio(
    "Navigate",
    ("Data Overview", "BLS Salary Model", "BLS+LinkedIn Salary Model")
)

st.sidebar.markdown("---")
st.sidebar.markdown("[GitHub Repo](https://github.com/IhwaHussain/Job-Salary-Analytics)")

##### --- UTILS -----
def salary_range(pred, delta=0.08):
    return int(pred * (1 - delta)), int(pred * (1 + delta))

##### 1. Data Overview -----
if page == "Data Overview":
    st.title("Labor Data Overview")
    st.write("Explore combined BLS, ILO, and (optionally) LinkedIn job salary data.")

    with st.expander("Raw Data Preview"):
        st.write("BLS data", bls_df.head())
        if ilo_df is not None:
            st.write("ILO data", ilo_df.head())
        if li_df is not None:
            st.write("LinkedIn data", li_df.head())

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

    st.subheader("Highest Demand Industries")
    if 'Industry' in bls_df.columns:
        top_industries = bls_df['Industry'].value_counts().head(10)
        fig = px.bar(top_industries, orientation='h', title="Top 10 Highest Demand Industries")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Salary Trends (2023–2024)")
    if 'Year' in bls_df.columns:
        trend = bls_df.groupby('Year')['Salary'].mean().reset_index()
        fig = px.line(trend, x='Year', y='Salary', markers=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Year column not found in BLS data for trend chart.")

##### 2. BLS Salary Model -----
elif page == "BLS Salary Model":
    st.title("BLS-Only Salary Prediction")
    st.write("Predict expected salary with job title, region, and experience, based on BLS data.")

    col1, col2 = st.columns(2)

    with col1:
        job_title = st.selectbox("Job Title", bls_df['Job Title'].unique())
        region = st.selectbox("Region", bls_df['Region'].unique())
    with col2:
        experience = st.slider("Experience Level (years)", 0, 40, 2)

    if st.button("Predict Salary (BLS Model)"):
        try:
            model = model_bls.load_model()
            pred = model_bls.predict_salary(job_title, region, experience, model)
            low, high = salary_range(pred)
            st.success(f"Estimated salary for '{job_title}' in {region} with {experience} yrs exp: **${low:,}–${high:,}**")
        except Exception as e:
            st.error(f"Prediction error: {e}")

    st.markdown("---")
    st.subheader("Model Insights (BLS)")
    st.write("Feature importance, salary distribution, and region breakdown.")

    fig = px.box(bls_df, x='Region', y='Salary', color='Region', points='all')
    st.plotly_chart(fig, use_container_width=True)

##### 3. BLS + LinkedIn Salary Model -----
elif page == "BLS+LinkedIn Salary Model":
    st.title("BLS + LinkedIn Salary Prediction")
    st.write("Leverages features from BLS and LinkedIn for improved accuracy.")

    if li_df is not None:
        job_title = st.selectbox("Job Title", li_df["Job Title"].unique())
        region = st.selectbox("Region", li_df["Region"].unique())
        industry = st.selectbox("Industry", li_df["Industry"].unique())
        experience = st.slider("Experience Level (years)", 0, 40, 2)
    else:
        st.warning("LinkedIn data not found. Prediction form disabled.")
        job_title, region, industry, experience = None, None, None, None

    if st.button("Predict Salary (BLS+LI Model)") and li_df is not None:
        try:
            model = model_bls_li.load_model()
            pred = model_bls_li.predict_salary(job_title, region, experience, industry, model)
            low, high = salary_range(pred)
            st.success(f"Estimated salary for '{job_title}' ({industry}) in {region} with {experience} yrs exp: **${low:,}–${high:,}**")
        except Exception as e:
            st.error(f"Prediction error: {e}")

    if li_df is not None:
        st.markdown("---")
        st.subheader("Industry-Wise Salary Distribution")
        fig = px.violin(li_df, x="Industry", y="Salary", color="Region")
        st.plotly_chart(fig, use_container_width=True)


         
       

   



  
