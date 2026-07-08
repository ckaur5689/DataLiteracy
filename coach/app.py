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

user_input = st.text_area(
    "Describe the data question, dashboard, pathway or decision you're working on:",
    placeholder="Example: We introduced a frailty pathway and admissions appear lower. Has it worked?"
)

# ------------------------------------------------------
# Recommendations
# ------------------------------------------------------

if st.button("Recommend Modules"):

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
