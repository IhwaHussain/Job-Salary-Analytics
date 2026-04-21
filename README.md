# Job Salary Analytics

[![license MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io)
[![🚀 Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Open_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://job-salary-analytics-lvlkp6ty5chlcqkqcy9kcr.streamlit.app)

---

## Table of Contents
- [Overview](#overview)
- [Key Findings](#key-findings)
- [Data Sources](#data-sources)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [License](#license)

---

## Overview

**Job Salary Analytics** is a data analytics project exploring employment and salary trends using occupational wage data structures inspired by the Bureau of Labor Statistics (BLS) and LinkedIn job postings. The project features an interactive Streamlit web app with salary distribution charts, regional breakdowns, and an ML-powered salary prediction model.

> ⚠️ **Note:** Currently running with sample data — real dataset integration in progress.

The analysis covers:
- Job status and classifications
- Wages and compensation trends
- Recruitment patterns and labor participation
- Salary transparency practices
- Prevalence and trends in remote work

---

## Key Findings

- **Transparency & Recruitment:** A significant proportion of job postings opt for non-transparent salary disclosure, potentially limiting candidate engagement and market comparability.
- **Sector-specific Insights:** Retail, Wholesale, and Finance sectors display higher working hours with lower average pay. Education sectors tend to reward increased work hours with commensurately higher pay.
- **Salary Discrepancy:** ML-based analysis uncovers discrepancies between advertised salary ranges and standardized government wage data, underscoring challenges in wage normalization.
- **Remote Work & Participation:** Patterns in remote job listings and labor force participation rates provide insight into evolving post-pandemic workplace dynamics.

---

## Data Sources

- **Bureau of Labor Statistics (BLS):** [Occupational Employment and Wage Statistics](https://www.bls.gov/oes/)
- **International Labour Organization (ILO):** [Short-Term Labour Force Statistics](https://www.ilo.org/stats)

---

## Architecture

```
[Sample Data / BLS CSV]
        |
        ▼
[Pandas Data Ingestion & Cleaning]
        |
        ▼
[scikit-learn ML Modeling]
        |
        ▼
[Streamlit Web App + Plotly Visualizations]
```

---

## Technology Stack

- **Processing:** Python, Pandas, scikit-learn
- **Web App:** Streamlit
- **Visualization:** Plotly
- **Data Management:** CSV, BLS public data sources

---

## Setup and Installation

### Prerequisites
- Python 3.10+

### Installation Steps

1. Clone the repository
```bash
git clone https://github.com/IhwaHussain/Job-Salary-Analytics.git
cd Job-Salary-Analytics
```

2. Set up Python environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your browser
2. Navigate between **Data Overview** and **BLS Salary Model** using the sidebar
3. Explore salary distributions by job title and region
4. Use the prediction form to estimate salary based on job title, region, and experience

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

