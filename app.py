import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ------------------ Database connection ------------------
engine = create_engine(
    "postgresql+psycopg2://postgres:Malu%401811@localhost:5432/phonepe"
)

st.set_page_config(page_title="PhonePe BI Dashboard", layout="wide")

# ------------------ Sidebar ------------------
menu = st.sidebar.radio("Menu", ["Executive Summary", "Dashboard"])

# =========================================================
#                  EXECUTIVE SUMMARY
# =========================================================
if menu == "Executive Summary":
    st.title("📊 PhonePe Business Intelligence Report")

    st.markdown("""
    ## Executive Summary

    This dashboard analyzes PhonePe user behavior and insurance adoption across India.

    ### Key Observations
    - Strong device concentration (Android dominates)
    - Uneven regional insurance growth
    - Large variation in user engagement

    ### Strategic Impact
    - Device optimization can improve performance for 70% users
    - Insurance vertical shows high revenue concentration
    - User engagement differs widely by geography

    ### Overall Recommendations
    - Focus marketing on top-performing states
    - Expand insurance in tier-2 cities
    - Optimize app for dominant devices
    """)

# =========================================================
#                      DASHBOARD
# =========================================================
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
        st.header("📱 Device Dominance & User Distribution")

        query = """
            SELECT brand, SUM(user_count) AS users
            FROM aggregated_user
            GROUP BY brand
            ORDER BY users DESC;
        """
        df1 = pd.read_sql(query, engine)

        col1, col2 = st.columns(2)
        col1.metric("Total Brands", df1.shape[0])
        col2.metric("Total Users", f"{int(df1['users'].sum()):,}")

        fig1 = px.bar(df1, x="brand", y="users",
                      title="Users by Device Brand")
        st.plotly_chart(fig1, use_container_width=True)

        fig1b = px.pie(df1, names="brand", values="users",
                       title="Market Share by Device Brand")
        st.plotly_chart(fig1b, use_container_width=True)

        st.subheader("🔍 Insights")
        st.write("""
        - Android brands dominate user base  
        - Top 3 brands contribute majority of users  
        - iOS penetration is minimal
        """)

        st.subheader("💡 Recommendations")
        st.write("""
        - Optimize for top Android devices  
        - Lightweight app for low-end phones  
        - OEM partnerships for pre-installs
        """)

    # ------------------ 2. Insurance Growth ------------------
    elif case == "2. Insurance Growth":
        st.header("📈 Insurance Growth Analysis")

        query = """
            SELECT state,
                   SUM(insurance_amount) AS total_amount,
                   SUM(insurance_count) AS total_policies
            FROM aggregated_insurance
            GROUP BY state
            ORDER BY total_amount DESC;
        """
        df2 = pd.read_sql(query, engine)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Insurance Value", f"₹ {int(df2.total_amount.sum()):,}")
        col2.metric("Total Policies", f"{int(df2.total_policies.sum()):,}")
        col3.metric("Top State", df2.iloc[0]["state"])

        fig2 = px.bar(df2.head(10), x="state", y="total_amount",
                      title="Top 10 States by Insurance Amount")
        st.plotly_chart(fig2, use_container_width=True)

        fig2b = px.pie(df2.head(5), names="state", values="total_amount",
                       title="Top 5 States Contribution")
        st.plotly_chart(fig2b, use_container_width=True)

        st.subheader("🔍 Insights")
        st.write("""
        - Southern states dominate insurance revenue  
        - Huge gap between top and bottom states  
        - Strong concentration risk
        """)

        st.subheader("💡 Recommendations")
        st.write("""
        - Expand in tier-2 cities  
        - Micro-insurance for rural users  
        - Cross-sell via UPI
        """)

    # ------------------ 3. User Engagement ------------------
    elif case == "3. User Engagement":
        st.header("📱 User Engagement Analysis")

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
            title="Users vs Engagement"
        )
        st.plotly_chart(fig3, use_container_width=True)

        fig32 = px.bar(df3.sort_values("app_opens", ascending=False).head(10),
                       x="state", y="app_opens",
                       title="Top 10 States by App Opens")
        st.plotly_chart(fig32, use_container_width=True)

        st.subheader("🔍 Insights")
        st.write("""
        - Registration ≠ engagement  
        - Metro states show highest activity  
        - Many dormant users exist
        """)

        st.subheader("💡 Recommendations")
        st.write("""
        - Cashback & retention campaigns  
        - Personalized regional offers  
        - Gamification for daily usage
        """)

    # ------------------ 4. Insurance Engagement ------------------
    elif case == "4. Insurance Engagement":
        st.header("🛡️ Insurance Engagement")

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
                           title="Insurance Revenue Tree")
        st.plotly_chart(fig42, use_container_width=True)

        st.subheader("🔍 Insights")
        st.write("""
        - Few states generate most revenue  
        - High policy count ≠ high value
        """)

        st.subheader("💡 Recommendations")
        st.write("""
        - Upsell premium plans  
        - Educate low-performing states
        """)

    # ------------------ 5. Top User Registration ------------------
    elif case == "5. Top User Registration":
        st.header("👥 Top User Registration")

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

        st.subheader("🔍 Insights")
        st.write("""
        - Urban districts dominate growth  
        - Rural adoption still low  
        - IT hubs lead new registrations
        """)

        st.subheader("💡 Recommendations")
        st.write("""
        - Rural-first onboarding  
        - Regional language support  
        - Offline agent partnerships
        """)
