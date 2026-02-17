  **📊PhonePe Business Intelligence Dashboard**

**📌 Project Overview****

This is an end-to-end Business Intelligence (BI) project built using PhonePe Pulse data.
The objective of this project is to analyze user behavior, digital transactions, and insurance adoption trends across India and present actionable insights through an interactive dashboard.

**The project demonstrates the complete BI pipeline:**

Data Collection → Data Engineering → Data Storage → Data Analysis → Data Visualization

**🎯 Business Objectives**

1. Understand device usage patterns across states

2. Analyze insurance growth trends

3. Measure user engagement levels

4. Identify top-performing regions

5. Support data-driven business decisions

**🧰 Tech Stack**

Category	Tools

   *Programming	Python

   *Data Handling	Pandas, JSON

   *Database	PostgreSQL

   *ORM	SQLAlchemy

   *Dashboard	Streamlit

   *Visualization	Plotly

   *Version Control	Git, GitHub

   *📂 Dataset

**Data is sourced from the official PhonePe Pulse GitHub Repository, which contains: Transaction data, User data, Insurance data in JSON format, structured by:

State → Year → Quarter**

 **🔄 Project Workflow (ETL Pipeline)**

1. Data Collection

Cloned the PhonePe Pulse repository using GitPython.

2. Data Extraction

Read nested JSON files using:

os.listdir()

json.load()

Iterated through state, year, and quarter folders.

3. Data Transformation

Converted raw JSON into structured Pandas DataFrames:

aggregated_transaction

aggregated_user

aggregated_insurance

map_transaction

map_user

map_insurance

top_user

top_insurance

4. Data Storage

Stored all DataFrames into PostgreSQL using SQLAlchemy.

Enabled fast SQL querying for dashboard.

5. Data Visualization

Built an interactive dashboard using Streamlit + Plotly

Added filters for:

State

Year

Quarter

Top N records

📊 Business Use Cases Implemented
1. Device Dominance

Analyzes:

Most used mobile brands

Total users vs app opens

2. Insurance Growth

Analyzes:

State-wise insurance revenue

Policy adoption trends

3. User Engagement

Analyzes:

Registered users vs app activity

High and low engagement districts

4. Insurance Engagement

Analyzes:

District-level insurance usage

Revenue contribution

5. Top User Registration

Analyzes:

Top districts and pincodes by registrations

**📈 Key KPIs**

Total Registered Users

Total App Opens

Engagement Ratio

Total Insurance Amount

Total Transactions

**🔍 Key Insights**

Android devices dominate the user base.

Metro cities show significantly higher engagement.

Insurance adoption is concentrated in a few states.

Several regions have high users but low engagement.

**💡 Business Recommendations**

Launch cashback and referral campaigns in low-engagement regions.

Introduce micro-insurance products in tier-2 cities.

Use regional language marketing.

Partner with device manufacturers for app promotions.

**🖥️ Dashboard Preview
**
The dashboard includes:

KPI cards

Bar charts

Scatter plots

Treemaps

Pie charts
with dynamic filters for better analysis.

**🚀 How to Run the Project**

Step 1: Clone the Repository
git clone https://github.com/your-username/your-repo-name.git

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Setup PostgreSQL

**Create database:**

CREATE DATABASE phonepe;


**Update DB connection in code:**

engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/phonepe")

Step 4: Run Streamlit App
streamlit run app.py

## 🏁 Conclusion

This project showcases:

Real-world data engineering

Strong SQL and Python integration

Practical business intelligence use cases

Professional dashboard design

It reflects how data can be transformed into meaningful business insights.

## Screenshots

![ Device Dominance](<img width="1057" height="450" alt="newplot (1)" src="https://github.com/user-attachments/assets/e7216cba-d7f7-4171-9136-5f0a3a7f7102" />)




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
Skills: Python, SQL, Data Visualization, BI Dashboards
 
