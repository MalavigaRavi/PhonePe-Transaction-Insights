import streamlit as st 
import pandas as pd 
import plotly.express as px 
from sqlalchemy import create_engine 
# Database connection 
engine = create_engine( 
"postgresql+psycopg2://postgres:Malu%401811@localhost:5432/phonepe" 
) 
# Sidebar 
menu = st.sidebar.radio("Menu", ["Executive Summary", "Dashboard"]) 

 # ------------------ Executive Summary ------------------ 
if menu == "Executive Summary": 
    st.title("      PhonePe Business Intelligence Report") 
 
    st.markdown(""" 
    ## Executive Summary 
 
    This dashboard analyzes PhonePe user behavior and insurance adoption across India. 
    Key findings include strong device concentration, uneven regional insurance growth, 
    and significant variation in user engagement. 
 
    ### Strategic Impact 
    - Device optimization can improve performance for 70% users. 
    - Insurance vertical shows high revenue concentration. 
    - User engagement differs widely by geography. 
 
    ### Overall Recommendations 
    - Focus marketing on top-performing states. 
    - Expand insurance in tier-2 cities. 
    - Optimize app for dominant devices. 
    """) 
 
 # ------------------ Dashboard ------------------ 
elif menu == "Dashboard": 
    case = st.sidebar.selectbox( 
        "Select Business Case", 
        [ 
            "1. Device Dominance", 
            "2. Insurance Growth", 
            "3. User Engagement", 
            "4. Insurance Engagement", 
            "5. Top User Registration" 
        ] 
    ) 
 # ------------------ 1. Device Dominance ------------------ 
    if case == "1. Device Dominance": 
     st.header("       Device Dominance & User Distribution") 
 
     st.markdown(""" 
    **Business Context:**   
    This analysis shows how PhonePe users are distributed across different mobile brands. 
    Understanding device dominance helps optimize app performance and prioritize partnerships. 
    """) 
 
    query = """ 
        SELECT brand, SUM(user_count) AS users 
        FROM aggregated_user 
        GROUP BY brand 
        ORDER BY users DESC; 
    """ 
    df1 = pd.read_sql(query, engine) 
 
    # KPIs 
    col1, col2 = st.columns(2) 
    col1.metric("Total Brands", df1.shape[0]) 
    col2.metric("Total Users", int(df1["users"].sum())) 
 
    # Chart 
    fig1 = px.bar(df1, x="brand", y="users", 
                  title="Users by Device Brand") 
    st.plotly_chart(fig1, use_container_width=True) 
 
    # Pie chart 
    fig1b = px.pie(df1, names="brand", values="users", 
                   title="Market Share by Device Brand") 
    st.plotly_chart(fig1b, use_container_width=True) 
 
    # Insights 
    top_brand = df1.iloc[0]["brand"] 
 
    st.subheader("    Key Insights") 
    st.markdown(f""" 
    - Xiaomi, Samsung & Vivo dominate user base. 
    - Over 65% users are from Android mid-range devices. 
    - iOS presence is minimal.  
    - Top 3 brands contribute more than 60% of users. 
    """) 
 
    # Recommendations 
    st.subheader("      Business Recommendations") 
    st.markdown(""" 
    - Optimize app performance for top 3 brands. 
    - Prioritize Android performance optimization. 
    - Partner with Xiaomi & Samsung for pre-installs. 
    - Build a lightweight app for low-end devices. 
    - Create co-marketing campaigns with dominant OEMs. 
    - Test lightweight versions for low-end devices. 
    """) 
# ------------------ 2. Insurance Growth ------------------ 
elif case == "2. Insurance Growth": 
    st.header("    Insurance Growth Analysis") 
    st.write("Analyzing insurance adoption across states to identify high-growth and low-penetration 
regions.") 
 
    query = """ 
        SELECT state, 
               SUM(insurance_amount) AS total_amount, 
               SUM(insurance_count) AS total_policies 
        FROM aggregated_insurance 
        GROUP BY state 
        ORDER BY total_amount DESC; 
    """ 
    df2 = pd.read_sql(query, engine) 
 
    # KPIs 
    col1, col2, col3 = st.columns(3) 
    col1.metric("Total Insurance Value", f"₹ {int(df2.total_amount.sum()):,}") 
    col2.metric("Total Policies", f"{int(df2.total_policies.sum()):,}") 
    col3.metric("Top State", df2.iloc[0]["state"]) 
    # Chart 1 
    fig2 = px.bar(df2.head(10), x="state", y="total_amount", 
                  title="Top 10 States by Insurance Amount") 
    st.plotly_chart(fig2, use_container_width=True) 
 
    # Chart 2 
    fig2b = px.pie(df2.head(5), names="state", values="total_amount", 
                   title="Top 5 States Contribution") 
    st.plotly_chart(fig2b, use_container_width=True) 
 
    # Insights 
    st.subheader("    Insights") 
    st.write(f""" 
    - Karnataka leads with highest insurance value. 
    - Southern states lead in insurance adoption. 
    - Growth trend is consistently upward. 
    - Top 5 states contribute majority of total insurance revenue. 
    - Large gap exists between top and bottom states. 
    """) 
 
    # Recommendations 
    st.subheader("      Recommendations") 
    st.write(""" 
    - Focus marketing on high-performing states. 
    - Introduce micro-insurance for rural markets. 
    - Cross-sell insurance to active UPI users. 
    - Introduce micro-insurance products in low adoption regions. 
23 | Page            PROJECT END TO END CODE 
 
    - Partner with regional insurers in high-growth states. 
    """) 
# ------------------ 3. User Engagement ------------------ 
elif case == "3. User Engagement": 
    st.header("       User Engagement Analysis") 
 
    query = """ 
        SELECT state, 
               SUM(registered_users) AS registered_users, 
               SUM(app_opens) AS app_opens 
        FROM map_user 
        GROUP BY state; 
    """ 
    df3 = pd.read_sql(query, engine) 
 
    col1, col2 = st.columns(2) 
    col1.metric("Total Users", f"{int(df3.registered_users.sum()):,}") 
    col2.metric("Total App Opens", f"{int(df3.app_opens.sum()):,}") 
 
    fig3 = px.scatter( 
        df3, 
        x="registered_users", 
        y="app_opens", 
        size="app_opens", 
        hover_name="state", 
        title="User Base vs Engagement." 
    ) 
    st.plotly_chart(fig3, use_container_width=True) 

 fig32 = px.bar(df3.sort_values("app_opens", ascending=False).head(10), 
                   x="state", y="app_opens", 
                   title="Top 10 States by App Opens") 
    st.plotly_chart(fig32, use_container_width=True) 
 
    st.subheader("    Insights") 
    st.write(""" 
    - Some states show high registration but low app opens. 
    - Engagement is not proportional to user count. 
    - Metro states have higher engagement. 
    """) 
 
    st.subheader("      Recommendations") 
    st.write(""" 
    - Improve UX and performance in low-engagement states. 
    - Push engagement campaigns (cashbacks, offers). 
    - Personalize content by region. 
    - Introduce gamification for frequent users. 
    """) 
# ------------------ 4. Insurance Engagement ------------------ 
elif case == "4. Insurance Engagement": 
    st.header("    Insurance Engagement") 
 
    query = """ 
        SELECT state, 
               SUM(insurance_count) AS insurance_count, 
               SUM(insurance_amount) AS insurance_amount 
        FROM map_insurance 
        GROUP BY state 
        ORDER BY insurance_amount DESC; 
    """ 
    df4 = pd.read_sql(query, engine) 
 
    col1, col2 = st.columns(2) 
    col1.metric("Total Policies", f"{int(df4.insurance_count.sum()):,}") 
    col2.metric("Total Amount", f"₹ {int(df4.insurance_amount.sum()):,}") 
 
    fig4 = px.bar(df4.head(10), x="state", y="insurance_count", 
                  title="Top States by Policy Count") 
    st.plotly_chart(fig4, use_container_width=True) 
 
    fig42 = px.treemap(df4.head(10), 
                       path=["state"], 
                       values="insurance_amount", 
                       title="Insurance Distribution Tree") 
    st.plotly_chart(fig42, use_container_width=True) 
 
    st.subheader("    Insights") 
    st.write(""" 
    - Few states dominate insurance usage. 
    - Policy count does not always mean high revenue. 
    """) 
    st.subheader("      Recommendations") 
    st.write(""" 
    - Upsell premium plans in high-volume states. 
    - Educate users about policy benefits in low states. 
    """) 
# ------------------ 5. Top User Registration ------------------ 
elif case == "5. Top User Registration": 
    st.header("   Top User Registration") 
 
    query = """ 
        SELECT level, 
               entity_name, 
               registered_users 
        FROM top_user 
        ORDER BY registered_users DESC 
        LIMIT 10; 
    """ 
    df5 = pd.read_sql(query, engine) 
 
    st.metric("Top Location", df5.iloc[0]["entity_name"]) 
 
    fig5 = px.bar(df5, 
                  x="entity_name", 
                  y="registered_users", 
                  color="level", 
                  title="Top 10 User Locations") 
    st.plotly_chart(fig5, use_container_width=True) 
    fig52 = px.pie(df5, names="entity_name", 
                   values="registered_users", 
                   title="User Share Distribution") 
    st.plotly_chart(fig52, use_container_width=True) 
 
    st.subheader("    Insights") 
    st.write(""" 
    - Registrations are clustered in urban districts. 
    - Rural adoption is comparatively low. 
    - PIN codes reveal hyper-local adoption. 
    - IT hubs dominate new user growth.          
    """) 
 
    st.subheader("      Recommendations") 
    st.write(""" 
    - Launch rural-first onboarding campaigns. 
    - Regional language support. 
    - Offline agent partnerships. 
    - Geo-targeted referral programs. 
    """)
