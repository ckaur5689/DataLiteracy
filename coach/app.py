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

st.header("Start coaching")

st.markdown("""
Choose a common question below, or describe your own data question in the box.
""")

example_questions = [
    "We introduced a frailty pathway and admissions appear lower. Has it worked?",
    "I am reviewing a dashboard and I am not sure whether the trend is meaningful.",
    "We want to compare performance between places with different populations.",
    "I need to understand whether average length of stay is misleading.",
    "I am considering whether a predictive model or risk stratification tool is safe to use.",
    "We are trying to understand demand, capacity and flow across a pathway.",
    "I want to know whether a pilot scheme delivered value for money.",
    "I need to understand inequalities across a population group."
]

selected_example = st.selectbox(
    "Useful starting questions",
    [""] + example_questions,
    index=0
)

user_input = st.text_area(
    "Or describe your own data question, dashboard, pathway or decision:",
    value=selected_example,
    placeholder="Example: We introduced a frailty pathway and admissions appear lower. Has it worked?",
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
