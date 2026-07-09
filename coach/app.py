import streamlit as st
from pathlib import Path
from styles import load_css
from components import module_card
from modules import load_modules, recommend_modules

# ------------------------------------------------------
# Page configuration
# ------------------------------------------------------

st.set_page_config(
    page_title="Health Data Literacy Companion",
    page_icon="📊",
    layout="wide"
)

load_css()

# ------------------------------------------------------
# Paths
# ------------------------------------------------------

repo_root = Path(__file__).parent.parent
book_cover = repo_root / "images" / "BookCover.png"

# ------------------------------------------------------
# Landing page
# ------------------------------------------------------

st.markdown("""
<div class="top-panel">

<h1 class="hero-title">
Health Data Literacy Companion
</h1>

<p class="hero-subtitle">
Helping healthcare leaders ask better questions.
</p>

<div class="hero-badge">
📘 Companion to the Health Data Literacy Programme
</div>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# Challenge cards
# ------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊\n\nDashboard Interpretation", use_container_width=True):
        st.session_state.selected_question = (
            "I am reviewing a dashboard and I am not sure whether the trend is meaningful."
        )

with col2:
    if st.button("🧪\n\nEvaluation & Evidence", use_container_width=True):
        st.session_state.selected_question = (
            "We introduced a frailty pathway and admissions appear lower. Has it worked?"
        )

with col3:
    if st.button("👥\n\nPopulation Health", use_container_width=True):
        st.session_state.selected_question = (
            "We want to compare performance between places with different populations."
        )

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🤖\n\nAI & Analytics", use_container_width=True):
        st.session_state.selected_question = (
            "I am considering whether a predictive model or risk stratification tool is safe to use."
        )

with col2:
    if st.button("🏥\n\nDemand & Capacity", use_container_width=True):
        st.session_state.selected_question = (
            "We are trying to understand demand, capacity and flow across a pathway."
        )

with col3:
    if st.button("💷\n\nHealth Economics", use_container_width=True):
        st.session_state.selected_question = (
            "I want to know whether a pilot scheme delivered value for money."
        )

st.markdown("### Or describe your own challenge")

user_input = st.text_area(
    "Type or edit your question:",
    key="selected_question",
    height=120
)

# ------------------------------------------------------
# Recommendations
# ------------------------------------------------------

if st.button("Recommend Modules", type="primary"):

    if not user_input.strip():
        st.warning("Please describe your question first.")

    else:
        recommendations = recommend_modules(user_input)

        if len(recommendations) == 0:
            st.warning(
                "No matching modules were found.\n\n"
                "Try including words such as evaluation, dashboard, rates, variation, AI, inequalities or population."
            )

        else:
            st.subheader("Recommended Modules")

            for module in recommendations:
                module_card(module)

# ------------------------------------------------------
# Module library
# ------------------------------------------------------

st.divider()

st.header("Browse Module Library")

modules = load_modules()

pathways = sorted(
    list(
        set(
            module["pathway"]
            for module in modules
        )
    )
)

selected_pathway = st.selectbox(
    "Learning pathway",
    ["All"] + pathways
)

for module in modules:

    if (
        selected_pathway == "All"
        or module["pathway"] == selected_pathway
    ):

        with st.expander(module["title"]):

            st.write(f"**Learning pathway:** {module['pathway']}")

            st.write("**Keywords**")

            st.write(", ".join(module["keywords"]))

            if "module_url" in module:
                st.link_button(
                    "Open Module",
                    module["module_url"]
                )
