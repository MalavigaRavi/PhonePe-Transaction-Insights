# PhonePe Transaction Insights

An end-to-end data analytics project that uses PhonePe Pulse data to analyze digital payment behavior across India, implemented in Python, SQL, PostgreSQL, and Streamlit.

## Project Overview

This project analyzes transaction, user, and insurance data from the official PhonePe Pulse dataset. The data is extracted from JSON files, transformed using Python, stored in PostgreSQL, and visualized through an interactive Streamlit dashboard to generate business insights.

## Business Problem

With increasing digital payment adoption, businesses need to understand:
- User behavior
- Regional performance
- Insurance penetration
- Device usage patterns

This project aims to provide data-driven insights to support strategic decision-making.

## Tech Stack

- Python  
- PostgreSQL  
- SQL  
- Pandas  
- Streamlit  
- Plotly  
- Git & GitHub

## Project Architecture

PhonePe Pulse Data (GitHub)  
→ Python ETL  
→ PostgreSQL Database  
→ SQL Queries  
→ Streamlit Dashboard

## Data Pipeline

### Data Extraction
Data is cloned from the official PhonePe Pulse GitHub repository and JSON files are parsed using Python.

### Data Transformation
JSON files are converted into Pandas DataFrames, cleaned, and standardized.

### Data Loading
Transformed data is stored into PostgreSQL tables using SQLAlchemy.

## Database Tables

- aggregated_transaction  
- aggregated_user  
- aggregated_insurance  
- map_transaction  
- map_user  
- map_insurance  
- top_state_transaction  
- top_user  
- top_insurance  

## Dashboard Features

1. Device Dominance – User distribution by mobile brand  
2. Insurance Growth – Top states by insurance revenue  
3. User Engagement – App opens vs registrations  
4. Insurance Engagement – Policy count analysis  
5. Top Locations – District and pincode insights

## Key Business Insights

- Top 3 brands contribute over 60% of users  
- Southern states dominate insurance adoption  
- Engagement varies significantly by region  
- Insurance revenue is concentrated in a few states  

## Business Recommendations

- Focus marketing on high-performing states  
- Introduce micro-insurance in tier-2 cities  
- Optimize app for dominant Android brands  
- Launch rural onboarding campaigns  

## How to Run This Project

1. Clone repository  
git clone https://github.com/yourusername/PhonePe-Transaction-Insights.git

2. Install libraries  
pip install -r requirements.txt

3. Run ETL  
python phonepe_etl.py

4. Run dashboard  
streamlit run app.py

## Screenshots

(Add your Streamlit dashboard images here)

![Dashboard](screenshots/dashboard1.png)

## Learning Outcomes

- Built end-to-end ETL pipeline  
- Improved SQL analytics skills  
- Developed business dashboards  
- Gained experience with PostgreSQL

## Dataset

PhonePe Pulse  
https://github.com/PhonePe/pulse

## Author

Malaviga Ravi  
Aspiring Data Analyst/Data Scientist  
Skills: Python | SQL | Streamlit | Power BI | Excel
 
