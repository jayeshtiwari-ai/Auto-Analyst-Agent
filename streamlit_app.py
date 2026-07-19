import os
import pandas as pd
import streamlit as st

from tools.loader import load_dataset
from tools.state import AgentState

from agents.profiler import profile_dataset
from tools.summary_builder import build_summary
from agents.cleaning_advisor import cleaning_advisor
from agents.cleaner import clean_dataset
from agents.analyzer import analyze_dataset
from agents.visualizer import visualize_dataset
from agents.insight import generate_insights
from agents.chat import chat_with_data

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Data Scientist Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# SESSION STATE
# ==========================================================

if "agent_state" not in st.session_state:
    st.session_state.agent_state = AgentState()

state = st.session_state.agent_state


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🤖 AI Data Scientist")

    st.markdown("---")

    st.markdown("### 🚀 Project")

    st.success("AI Powered Data Scientist")

    st.markdown("### 📌 Workflow")

    st.write("✔ Upload Dataset")
    st.write("✔ Profile Dataset")
    st.write("✔ Cleaning Advisor")
    st.write("✔ Data Cleaning")
    st.write("✔ Analysis")
    st.write("✔ Visualizations")
    st.write("✔ AI Insights")

    st.markdown("---")

    st.markdown("### 👨‍💻 Developer")

    st.info("Jayesh Tiwari")

    st.markdown("---")

    st.caption("Version 1.0")


# ==========================================================
# HEADER
# ==========================================================

st.title("🤖 AI Data Scientist Agent")

st.caption(
    "Analyze • Clean • Visualize • Generate AI Insights"
)

st.markdown("---")


# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📂 Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    os.makedirs(
        "data/uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "data/uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    df = load_dataset(file_path)

    if df is None:

        st.error("Unable to load dataset.")

        st.stop()

    state.set("dataset", df)

    profile_dataset(state)

    build_summary(state)

    profile = state.get("profile")


    # ==========================================================
    # KPI CARDS
    # ==========================================================

    st.markdown("## 📊 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        profile["rows"]
    )

    c2.metric(
        "Columns",
        profile["columns"]
    )

    c3.metric(
        "Missing",
        sum(profile["missing_values"].values())
    )

    c4.metric(
        "Duplicates",
        profile["duplicate_rows"]
    )

    st.markdown("---")


    # ==========================================================
    # TABS
    # ==========================================================

    preview_tab, cleaning_tab, analysis_tab, insight_tab, chat_tab = st.tabs(
        [
            "📄 Preview",
            "🧹 Cleaning",
            "📊 Analysis",
            "💡 AI Insights",
            "💬 Chat with Data"
        ]
    )

        # ==========================================================
    # PREVIEW TAB
    # ==========================================================

    with preview_tab:

        st.header("📄 Dataset Preview")

        st.dataframe(
            df.head(15),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        left, right = st.columns(2)

        # ---------------------------------------
        # Dataset Information
        # ---------------------------------------

        with left:

            st.subheader("📋 Dataset Information")

            info_df = pd.DataFrame(
                {
                    "Property": [
                        "Rows",
                        "Columns",
                        "Memory Usage (KB)"
                    ],
                    "Value": [
                        profile["rows"],
                        profile["columns"],
                        profile["memory_usage_kb"]
                    ]
                }
            )

            st.dataframe(
                info_df,
                use_container_width=True,
                hide_index=True
            )

        # ---------------------------------------
        # Missing Values
        # ---------------------------------------

        with right:

            st.subheader("⚠ Missing Values")

            missing_df = pd.DataFrame(
                profile["missing_values"].items(),
                columns=[
                    "Column",
                    "Missing Values"
                ]
            )

            st.dataframe(
                missing_df,
                use_container_width=True,
                hide_index=True
            )

        st.markdown("---")

        # ---------------------------------------
        # Numeric & Categorical Columns
        # ---------------------------------------

        left, right = st.columns(2)

        with left:

            st.subheader("🔢 Numeric Columns")

            if profile["numeric_columns"]:

                num_df = pd.DataFrame(
                    profile["numeric_columns"],
                    columns=["Column Name"]
                )

                st.dataframe(
                    num_df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info("No Numeric Columns")

        with right:

            st.subheader("📝 Categorical Columns")

            if profile["categorical_columns"]:

                cat_df = pd.DataFrame(
                    profile["categorical_columns"],
                    columns=["Column Name"]
                )

                st.dataframe(
                    cat_df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info("No Categorical Columns")

        st.markdown("---")

        # ---------------------------------------
        # Data Types
        # ---------------------------------------

        st.subheader("🧾 Data Types")

        dtype_df = pd.DataFrame(
            profile["data_types"].items(),
            columns=[
                "Column",
                "Data Type"
            ]
        )

        st.dataframe(
            dtype_df,
            use_container_width=True,
            hide_index=True
        )

            # ==========================================================
    # CLEANING TAB
    # ==========================================================

    with cleaning_tab:

        st.header("🧹 AI Cleaning Advisor")

        st.write(
            "Generate an AI-powered cleaning plan, review the recommendations, "
            "and clean your dataset with one click."
        )

        st.markdown("")

        # ------------------------------------------------------
        # Generate Cleaning Plan
        # ------------------------------------------------------

        if st.button(
            "🤖 Generate Cleaning Plan",
            use_container_width=True
        ):

            with st.spinner("Analyzing dataset..."):

                cleaning_advisor(state)

            st.success("Cleaning plan generated successfully!")

        plan = state.get("cleaning_plan")

        # ------------------------------------------------------
        # Show Cleaning Recommendations
        # ------------------------------------------------------

        if plan:

            st.markdown("---")

            st.subheader("📋 AI Recommendations")

            for column, details in plan.items():

                issue = details.get("issue", "N/A")
                recommendation = details.get("recommendation", "N/A")
                reason = details.get("reason", "N/A")

                with st.container(border=True):

                    c1, c2 = st.columns([3, 1])

                    with c1:

                        st.markdown(f"### 📌 {column}")

                        st.write(f"**Issue:** {issue}")

                        st.write(
                            f"**Recommendation:** {recommendation}"
                        )

                        st.write(f"**Reason:** {reason}")

                    with c2:

                        st.success("Recommended")

            st.markdown("")

            # --------------------------------------------------
            # Apply Cleaning
            # --------------------------------------------------

            if st.button(
                "🧹 Apply Cleaning",
                type="primary",
                use_container_width=True
            ):

                with st.spinner("Cleaning dataset..."):

                    clean_dataset(state)

                st.success("Dataset cleaned successfully!")

        # ------------------------------------------------------
        # Cleaned Dataset Preview
        # ------------------------------------------------------

        cleaned_df = state.get("cleaned_dataset")

        if cleaned_df is not None:

            st.markdown("---")

            st.subheader("✅ Cleaned Dataset Preview")

            st.dataframe(
                cleaned_df.head(15),
                use_container_width=True,
                hide_index=True
            )

            csv = cleaned_df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇ Download Cleaned Dataset",
                csv,
                "cleaned_dataset.csv",
                "text/csv",
                use_container_width=True
            )

                # ==========================================================
    # ANALYSIS TAB
    # ==========================================================

    with analysis_tab:

        st.header("📊 Data Analysis Dashboard")

        cleaned_df = state.get("cleaned_dataset")

        if cleaned_df is None:

            st.info("🧹 Please clean the dataset first.")

        else:

            with st.spinner("Analyzing dataset..."):

                analyze_dataset(state)
                visualize_dataset(state)

            analysis = state.get("analysis")

            # ==========================================================
            # AI INSIGHTS TAB
            # ==========================================================

            with insight_tab:

                st.header("💡 AI Business Insights")

                cleaned_df = state.get("cleaned_dataset")

                if cleaned_df is None:

                    st.info("🧹 Please clean the dataset first.")

                else:

                    if st.button(
                        "🤖 Generate AI Insights",
                        use_container_width=True
                    ):

                        with st.spinner("Generating AI insights..."):

                            analyze_dataset(state)      # Ensure analysis exists
                            generate_insights(state)

                        st.success("Insights Generated Successfully!")

                    insights = state.get("insights")

                    if insights:

                        st.markdown("---")

                        st.markdown(
                            f"""
            <div style="
            padding:20px;
            border-radius:10px;
            background-color:#f8f9fa;
            border:1px solid #d9d9d9;
            font-size:16px;
            line-height:1.7;">
            {insights}
            </div>
            """,
                            unsafe_allow_html=True
                        )

            # ==========================================
            # KPI SUMMARY
            # ==========================================

            st.subheader("📈 Analysis Summary")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Rows",
                analysis["rows"]
            )

            c2.metric(
                "Columns",
                analysis["columns"]
            )

            c3.metric(
                "Missing Values",
                sum(analysis["missing_values"].values())
            )

            st.markdown("---")

            # ==========================================
            # STATISTICS
            # ==========================================

            st.subheader("📋 Statistical Summary")

            stats_df = pd.DataFrame(
                analysis["statistics"]
            )

            st.dataframe(
                stats_df,
                use_container_width=True
            )

            st.markdown("---")

            # ==========================================
            # CORRELATION MATRIX
            # ==========================================

            st.subheader("🔥 Correlation Matrix")

            corr_df = pd.DataFrame(
                analysis["correlation"]
            )

            st.dataframe(
                corr_df,
                use_container_width=True
            )

            st.markdown("---")

            # ==========================================
            # CHARTS
            # ==========================================

            # ==========================================================
            # VISUALIZATIONS
            # ==========================================================

            st.subheader("📊 Visualizations")

            # -------------------------------
            # First Row
            # -------------------------------

            col1, col2 = st.columns(2)

            with col1:

                with st.container(border=True):

                    st.markdown("#### 📈 Distribution")

                    if os.path.exists("outputs/distribution.png"):

                        st.image(
                            "outputs/distribution.png",
                            use_container_width=True
                        )
                    else:
                        st.info("Distribution chart not available.")

            with col2:

                with st.container(border=True):

                    st.markdown("#### 🔥 Correlation Heatmap")

                    if os.path.exists("outputs/correlation_heatmap.png"):

                        st.image(
                            "outputs/correlation_heatmap.png",
                            use_container_width=True
                        )
                    else:
                        st.info("Heatmap not available.")


            # -------------------------------
            # Second Row
            # -------------------------------

            col3, col4 = st.columns(2)

            with col3:

                with st.container(border=True):

                    st.markdown("#### 📦 Box Plot")

                    if os.path.exists("outputs/boxplot.png"):

                        st.image(
                            "outputs/boxplot.png",
                            use_container_width=True
                        )
                    else:
                        st.info("Box plot not available.")

            with col4:

                with st.container(border=True):

                    st.markdown("#### 📊 Category Distribution")

                    if os.path.exists("outputs/categories.png"):

                        st.image(
                            "outputs/categories.png",
                            use_container_width=True
                        )
                    else:
                        st.info("Category chart not available.")


            # -------------------------------
            # Missing Values (only if present)
            # -------------------------------

            if os.path.exists("outputs/missing_values.png"):

                st.markdown("---")

                st.subheader("⚠ Missing Values")

                st.image(
                    "outputs/missing_values.png",
                    use_container_width=True
                )


                # ==========================================================
            # CHAT WITH DATA
            # ==========================================================

            with chat_tab:

                st.header("💬 Chat with Your Dataset")

                cleaned_df = state.get("cleaned_dataset")

                if cleaned_df is None:

                    st.info("Please clean the dataset first.")

                else:

                    if "messages" not in st.session_state:
                        st.session_state.messages = []

                    # Display previous messages
                    for message in st.session_state.messages:

                        with st.chat_message(message["role"]):
                            st.markdown(message["content"])

                    # User input
                    question = st.chat_input("Ask anything about your dataset...")

                    if question:

                        st.session_state.messages.append(
                            {
                                "role": "user",
                                "content": question
                            }
                        )

                        with st.chat_message("user"):
                            st.markdown(question)

                        with st.spinner("Thinking..."):

                            answer = chat_with_data(
                                state,
                                question
                            )

                        with st.chat_message("assistant"):
                            st.markdown(answer)

                        st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": answer
                            }
                        )