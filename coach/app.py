import streamlit as st
from pathlib import Path
from styles import load_css
from components import hero
from components import module_card
from modules import load_modules, recommend_modules

# ------------------------------------------------------
# Page configuration
# ------------------------------------------------------

st.set_page_config(
    page_title="Health Data Literacy Coach",
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
# Landing page header
# ------------------------------------------------------

hero(book_cover)

st.divider()

# ------------------------------------------------------
# User input
# ------------------------------------------------------

st.header("What are you trying to do today?")

st.markdown(
    "Choose a common challenge below, or type your own question further down."
)

if "selected_question" not in st.session_state:
    st.session_state.selected_question = ""

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "📊\n\nUnderstand a Dashboard",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "I am reviewing a dashboard and I am not sure whether the trend is meaningful."
        )

with col2:
    if st.button(
        "🧪\n\nEvaluate an Intervention",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "We introduced a frailty pathway and admissions appear lower. Has it worked?"
        )

with col3:
    if st.button(
        "👥\n\nPopulation Health",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "We want to compare performance between places with different populations."
        )

col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "🏥\n\nDemand & Capacity",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "We are trying to understand demand, capacity and flow across a pathway."
        )

with col2:
    if st.button(
        "🤖\n\nAI & Predictive Models",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "I am considering whether a predictive model or risk stratification tool is safe to use."
        )

with col3:
    if st.button(
        "💷\n\nHealth Economics",
        use_container_width=True
    ):
        st.session_state.selected_question = (
            "I want to know whether a pilot scheme delivered value for money."
        )

selected_example = st.selectbox(
    "Or choose one of these common questions",
    [""] + example_questions

selected_example = st.selectbox(
    "Or choose one of these common questions",
    [""] + example_questions
)

if selected_example:
    st.session_state.selected_question = selected_example

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
                "Try including words such as:\n"
                "- evaluation\n"
                "- dashboard\n"
                "- rates\n"
                "- variation\n"
                "- AI\n"
                "- inequalities\n"
                "- population"
            )

        else:

            st.subheader("Recommended Modules")

        for module in recommendations:

                    module_card(module)

                    st.write(f"**Learning pathway:** {module['pathway']}")

                    st.write("### Why this module?")

                    st.write(
                        "Matched keywords: "
                        + ", ".join(module["matched_keywords"])
                    )

                    st.write("### Questions to ask")

                    for question in module["questions"]:
                        st.markdown(f"- {question}")

                    if "module_url" in module:
                        st.link_button(
                            "Open Health Data Literacy Module",
                            module["module_url"]
                        )

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
