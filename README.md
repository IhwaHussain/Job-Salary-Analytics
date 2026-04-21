

# Job Salary Analytics

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Apache Spark](https://img.shields.io/badge/Spark-3.5.0-orange?logo=apache-spark)](https://spark.apache.org/)
[![Jupyter Notebooks](https://img.shields.io/badge/Jupyter-Notebook-important?logo=jupyter)](https://jupyter.org/)
[![Tableau](https://img.shields.io/badge/Tableau-Visualization-blueviolet?logo=tableau)](https://www.tableau.com/)

---
## 🔴 Live Demo
[![🚀 Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Open_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://job-salary-analytics-lvlkp6ty5chlcqkqcy9kcr.streamlit.app)
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

**Job Salary Analytics** is a comprehensive data analytics project that explores employment and recruitment trends using a blend of real-world job postings and governmental labor statistics. Leveraging over **124,000 job listings from 2023–2024** sourced from LinkedIn and cross-referenced with datasets from the Bureau of Labor Statistics (BLS) and the International Labour Organization (ILO), this project delivers actionable insights into the current employment landscape.

The analysis covers:
- Job status and classifications
- Wages and compensation trends
- Recruitment patterns and labor participation
- Salary transparency practices
- Prevalence and trends in remote work

---

## Key Findings

- **Transparency & Recruitment:**  
  A significant proportion of LinkedIn job postings opt for non-transparent salary disclosure and external (off-site) application processes, potentially limiting candidate engagement and market comparability.
- **Sector-specific Insights:**  
  - Retail, Wholesale, and Finance sectors display a trend of higher working hours with lower average pay.
  - In contrast, Education sectors tend to reward increased work hours with commensurately higher pay.
- **Salary Discrepancy:**  
  - ML-based analysis uncovers substantial discrepancies between salary ranges advertised on LinkedIn and standardized government salary data (BLS), underscoring challenges in wage normalization.
- **Remote Work & Participation:**  
  - Patterns in remote job listings and labor force participation rates provide insight into evolving post-pandemic workplace dynamics.

---

## Data Sources

- **LinkedIn Job Postings:**  
  Over 124,000 postings (2023–2024), scraped and anonymized.
- **Bureau of Labor Statistics (US, BLS):**  
  - [Current Employment Statistics](https://www.bls.gov/ces/)
  - [Occupational Employment and Wage Statistics](https://www.bls.gov/oes/)
- **International Labour Organization (ILO):**  
  - [Short-Term Labour Force Statistics](https://ilostat.ilo.org/data/)
  
---

## Architecture

```
[Data Ingestion]
     │
     ▼
[Apache Spark Processing]
     │
     ▼
[Query-based Analysis (Spark SQL)]
     │
     ▼
[MLLib ML Modeling]
     │
     ▼
[Tableau Visualization]
```

---

## Technology Stack

- **Processing:**  
  [Apache Spark](https://spark.apache.org/) (Core, SparkSQL, MLlib)
- **Programming/Analysis:**  
  [Jupyter Notebook](https://jupyter.org/) (Python, PySpark)
- **Visualization:**  
  [Tableau](https://www.tableau.com/)
- **Data Management:**  
  CSV, Parquet, and RESTful data sources

---

## Setup and Installation

### Prerequisites

- Python 3.8+
- Java 8+ (for Spark)
- [Apache Spark 3.5.0+](https://spark.apache.org/downloads.html)
- [Jupyter Notebook](https://jupyter.org/install)
- Tableau Desktop/Public (for visualization)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-org-or-username>/job-salary-analytics.git
   cd job-salary-analytics
   ```
2. **Set Up Python Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Install Apache Spark**
   - Follow [official guide](https://spark.apache.org/docs/latest/) to install Spark and configure the `SPARK_HOME` environment variable.
4. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
5. **(Optional) Download Tableau Desktop/Public**
   - Import sample output files or connect directly to processed datasets.

---

## Usage

1. **Data Ingestion:**  
   Place raw data in the `data/raw/` directory.
2. **Run Data Processing Notebooks:**  
   Open and execute the main notebooks in `notebooks/` to process and analyze the data.
3. **Machine Learning Models:**  
   Run `notebooks/modeling/` notebooks to reproduce ML analysis of salary discrepancies.
4. **Visualization:**  
   Use the exported processed data files (`output/`) in Tableau for advanced visualization, or load Tableau workbooks provided in `visualizations/`.
5. **Customization:**  
   Modify SQL queries, Spark jobs, or visualization dashboards to explore additional hypotheses or sectors.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
````
