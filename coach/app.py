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

st.markdown("## What challenge are you facing today?")

st.markdown(
    "Choose a common healthcare analytics challenge below, or describe your own."
)

if "selected_question" not in st.session_state:
    st.session_state.selected_question = ""

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
# Recommend button
# ------------------------------------------------------

st.markdown(
    "<p style='text-align:center; color:#6B7280;'>"
    "Ready to see which learning modules can help?"
    "</p>",
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    recommend = st.button(
        "🔍 Recommend My Learning Path",
        type="primary",
        use_container_width=True
    )

# ------------------------------------------------------
# Recommendations
# ------------------------------------------------------

if recommend:

    if not user_input.strip():
        st.warning("Please describe your question first.")

    else:

        recommendations = recommend_modules(user_input)

        if len(recommendations) == 0:

            st.warning(
                "No matching modules were found.\n\n"
                "Try including words such as evaluation, dashboard, variation, AI, inequalities or population."
            )

        else:

            st.subheader("📚 Recommended Modules")

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
