import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ------------------ Page Config ------------------
st.set_page_config(page_title="PhonePe BI Dashboard", layout="wide")

# ------------------ Database connection ------------------
engine = create_engine(
    "postgresql+psycopg2://postgres:Malu%401811@localhost:5432/phonepe"
)

# ------------------ Sidebar ------------------
menu = st.sidebar.radio("Menu", ["Executive Summary", "Dashboard"])

# =========================================================
# EXECUTIVE SUMMARY
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

    ### Strategic Value
    This analysis helps PhonePe:
    - Optimize app performance
    - Identify high-growth markets
    - Improve regional engagement
    - Drive insurance adoption
    """)

# =========================================================
# DASHBOARD
# =========================================================
elif menu == "Dashboard":

    # -------- GLOBAL FILTERS --------
    st.sidebar.subheader("🔎 Filters")

    states = pd.read_sql("SELECT DISTINCT state FROM aggregated_user", engine)["state"]
    years = pd.read_sql("SELECT DISTINCT year FROM aggregated_user", engine)["year"]

    selected_state = st.sidebar.multiselect("Select State", states)
    selected_year = st.sidebar.multiselect("Select Year", years)
    selected_quarter = st.sidebar.multiselect("Select Quarter", [1, 2, 3, 4])
    top_n = st.sidebar.slider("Top N", 5, 20, 10)

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

    # =====================================================
    # 1. Device Dominance
    # =====================================================
    if case == "1. Device Dominance":
        st.header("📱 Device Dominance & Engagement")

        query = """
        SELECT state, brand, year, quarter,
               SUM(user_count) AS total_users,
               SUM(app_opens) AS total_app_opens
        FROM aggregated_user
        GROUP BY state, brand, year, quarter
        """
        df = pd.read_sql(query, engine)

        if selected_state:
            df = df[df["state"].isin(selected_state)]
        if selected_year:
            df = df[df["year"].isin(selected_year)]
        if selected_quarter:
            df = df[df["quarter"].isin(selected_quarter)]

        df = df.sort_values("total_users", ascending=False).head(top_n)

        c1, c2 = st.columns(2)
        c1.metric("Total Users", int(df.total_users.sum()))
        c2.metric("Avg App Opens", int(df.total_app_opens.mean()))

        fig = px.bar(df, x="brand", y="total_users",
                     title="Top Device Brands by Users",
                     text_auto=True)
        st.plotly_chart(fig, width="stretch")

        st.subheader("🔍 Insights")
        st.markdown("""
        - Android brands dominate the user base.
        - A small number of brands contribute most users.
        - Some brands have high registrations but lower engagement.
        """)

        st.subheader("💡 Recommendations")
        st.markdown("""
        - Optimize app performance for top Android brands.
        - Partner with major OEMs for pre-install campaigns.
        - Build lightweight app version for low-end devices.
        """)

    # =====================================================
    # 2. Insurance Growth
    # =====================================================
    elif case == "2. Insurance Growth":
        st.header("📈 Insurance Growth")

        query = """
        SELECT state, year, quarter,
               SUM(insurance_amount) AS total_amount,
               SUM(insurance_count) AS total_policies
        FROM aggregated_insurance
        GROUP BY state, year, quarter
        """
        df = pd.read_sql(query, engine)

        if selected_state:
            df = df[df["state"].isin(selected_state)]
        if selected_year:
            df = df[df["year"].isin(selected_year)]
        if selected_quarter:
            df = df[df["quarter"].isin(selected_quarter)]

        df = df.sort_values("total_amount", ascending=False).head(top_n)

        fig = px.bar(df, x="state", y="total_amount",
                     title="Top States by Insurance Revenue",
                     text_auto=True)
        st.plotly_chart(fig, width="stretch")

        st.subheader("🔍 Insights")
        st.markdown("""
        - Insurance revenue is concentrated in few states.
        - Southern and metro states lead adoption.
        - Tier-2 states show emerging growth.
        """)

        st.subheader("💡 Recommendations")
        st.markdown("""
        - Focus marketing on top 5 states.
        - Launch micro-insurance products in tier-2 cities.
        - Bundle insurance with UPI and recharge offers.
        """)

    # =====================================================
    # 3. User Engagement
    # =====================================================
    elif case == "3. User Engagement":
        st.header("📊 User Engagement & Growth Strategy")

        st.markdown("""
        **Business Context:**  
        This analysis compares how many users are registered vs how actively they use the app.
        It helps identify **high-potential but low-engagement regions**.
        """)

        query = """
        SELECT state, hover_name,
            SUM(registered_users) AS registered_users,
            SUM(app_opens) AS app_opens
        FROM map_user
        GROUP BY state, hover_name
        """
        df = pd.read_sql(query, engine)

        # ---------------- KPIs ----------------
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Registered Users", f"{int(df.registered_users.sum()):,}")
        col2.metric("Total App Opens", f"{int(df.app_opens.sum()):,}")
        col3.metric("Avg Opens per User", 
                    round(df.app_opens.sum() / df.registered_users.sum(), 2))

        # ---------------- Chart 1: Scatter ----------------
        fig1 = px.scatter(
            df,
            x="registered_users",
            y="app_opens",
            size="app_opens",
            color="state",
            hover_name="hover_name",
            title="User Base vs Engagement by District"
        )
        st.plotly_chart(fig1, width="stretch")

        # ---------------- Chart 2: Top 10 Engagement ----------------
        top_engaged = df.sort_values("app_opens", ascending=False).head(10)

        fig2 = px.bar(
            top_engaged,
            x="hover_name",
            y="app_opens",
            color="state",
            title="Top 10 Districts by App Opens"
        )
        st.plotly_chart(fig2, width="stretch")

        # ---------------- Chart 3: Low Engagement ----------------
        df["engagement_ratio"] = df["app_opens"] / df["registered_users"]
        low_engagement = df.sort_values("engagement_ratio").head(10)

        fig3 = px.bar(
            low_engagement,
            x="hover_name",
            y="engagement_ratio",
            color="state",
            title="Bottom 10 Districts by Engagement Ratio"
        )
        st.plotly_chart(fig3, width="stretch")

        # ---------------- Insights ----------------
        st.subheader("🔍 Key Insights")
        st.markdown("""
        - Engagement is **not proportional** to registrations.
        - Metro districts show **very high activity levels**.
        - Several districts have **large user bases but poor engagement**.
        - Bottom districts show less than **0.5 opens per user on average**.
        """)

        # ---------------- Recommendations ----------------
        st.subheader("💡 Business Recommendations")
        st.markdown("""
        **Growth Strategy**
        - Target low-engagement districts with **cashback & referral campaigns**.
        - Use **regional language push notifications**.
        - Introduce **gamification (daily rewards, streaks)**.
        
        **Product Strategy**
        - Improve app performance in slow regions.
        - Personalize home screen by district usage patterns.
        
        **Marketing Strategy**
        - Focus ad spend on **high-user but low-engagement regions**.
        - Run district-level offers instead of national campaigns.
        """)

    # =====================================================
    # 4. Insurance Engagement
    # =====================================================
    elif case == "4. Insurance Engagement":
        st.header("🛡️ Insurance Engagement")

        query = """
        SELECT state, hover_name,
               SUM(insurance_count) AS insurance_count,
               SUM(insurance_amount) AS insurance_amount
        FROM map_insurance
        GROUP BY state, hover_name
        """
        df = pd.read_sql(query, engine)

        fig1 = px.bar(df.head(top_n),
                      x="hover_name",
                      y="insurance_amount",
                      title="Top Districts by Insurance Amount")
        st.plotly_chart(fig1, width="stretch")

        fig2 = px.treemap(df.head(20),
                          path=["state", "hover_name"],
                          values="insurance_amount",
                          title="Insurance Distribution")
        st.plotly_chart(fig2, width="stretch")

        st.subheader("🔍 Insights")
        st.markdown("""
        - Insurance usage is concentrated in few districts.
        - Policy count does not always mean high revenue.
        """)

        st.subheader("💡 Recommendations")
        st.markdown("""
        - Upsell premium insurance in high-volume districts.
        - Educate users in low-adoption regions.
        - Partner with local insurance agents.
        """)

    # =====================================================
    # 5. Top User Registration
    # =====================================================
    elif case == "5. Top User Registration":
        st.header("👥 Top User Registrations")

        query = """
        WITH ranked_users AS (
            SELECT 
                state,
                year,
                quarter,
                level,
                entity_name,
                SUM(registered_users) AS total_users,
                ROW_NUMBER() OVER (
                    PARTITION BY level
                    ORDER BY SUM(registered_users) DESC
                ) AS rank_no
            FROM top_user
            GROUP BY state, year, quarter, level, entity_name
        )
        SELECT *
        FROM ranked_users
        WHERE rank_no <= 10;
        """
        df = pd.read_sql(query, engine)

        fig1 = px.bar(df,
                      x="entity_name",
                      y="total_users",
                      color="level",
                      title="Top Locations by Registrations")
        st.plotly_chart(fig1, width="stretch")

        fig2 = px.pie(df,
                      names="entity_name",
                      values="total_users",
                      title="Registration Share")
        st.plotly_chart(fig2, width="stretch")

        st.subheader("🔍 Insights")
        st.markdown("""
        - Registrations are highly urban-centric.
        - District-level dominates user onboarding.
        - PIN-level shows hyper-local growth.
        """)

        st.subheader("💡 Recommendations")
        st.markdown("""
        - Launch rural-first onboarding campaigns.
        - Support regional languages.
        - Geo-target referral programs.
        """)
