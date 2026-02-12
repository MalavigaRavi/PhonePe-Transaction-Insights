PhonePe Transaction Insights 📊
**Project Overview**

PhonePe Transaction Insights is an end-to-end data analytics project that analyzes digital payment behavior across India using the official PhonePe Pulse dataset. The project focuses on extracting, transforming, storing, and visualizing large-scale transaction and user data to generate meaningful business insights.

The dashboard is built using Streamlit, with data stored in PostgreSQL and processed using Python and SQL.

**Business Problem**

With the rapid adoption of digital payments, organizations like PhonePe need to:

Understand user behavior

Identify high-performing regions

Track insurance adoption

Optimize device-level performance

Improve customer engagement

This project provides data-driven answers to these business questions.

Business Use Cases

Customer Segmentation

Fraud Pattern Analysis

Geographical Performance Tracking

Insurance Adoption Insights

User Engagement Monitoring

Product Optimization

Marketing Strategy Optimization

Tech Stack
   *Layer	Tools
   *Data Source	PhonePe Pulse (GitHub)
   *Language	Python
   *Database	PostgreSQL
   *Libraries	Pandas, SQLAlchemy, Plotly
   *Dashboard	Streamlit
   *Version Control	Git & GitHub
   *Project Architecture
   *PhonePe Pulse GitHub
        ↓
Python ETL Scripts
        ↓
PostgreSQL Database
        ↓
SQL Queries
        ↓
Streamlit Dashboard

Data Pipeline (ETL)
Step 1 – Data Extraction

Data is extracted from:
https://github.com/PhonePe/pulse

Using GitPython and JSON parsing.

Step 2 – Data Transformation

JSON files converted into DataFrames

Cleaned column names

Normalized formats

Step 3 – Load to PostgreSQL

Tables created:

aggregated_transaction

aggregated_user

aggregated_insurance

map_transaction

map_user

map_insurance

top_state_transaction

top_user

top_insurance

Dashboard Features
1. Device Dominance

User distribution by mobile brands

Market share analysis

2. Insurance Growth

Top states by insurance revenue

Policy adoption trends

3. User Engagement

Registered users vs App opens

Engagement scatter plots

4. Insurance Engagement

Policy count vs revenue

Treemap visualization

5. Top User Locations

Top districts & pincodes

Urban vs rural insights

Sample Business Insights

Top 3 brands contribute over 60% of users

Southern states dominate insurance adoption

High registration does not always mean high engagement

Insurance revenue is concentrated in few states

Urban districts lead new user growth

Business Recommendations

Optimize app for dominant Android devices

Focus insurance marketing on tier-2 cities

Introduce regional language onboarding

Partner with OEM brands

Launch rural-first referral campaigns
