import streamlit as st
from pathlib import Path
from modules import load_modules, recommend_modules

# ------------------------------------------------------
# Page configuration
# ------------------------------------------------------

st.set_page_config(
    page_title="Health Data Literacy Coach",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------------
# Paths
# ------------------------------------------------------

repo_root = Path(__file__).parent.parent
book_cover = repo_root / "images" / "BookCover.png"

# ------------------------------------------------------
# Landing page header
# ------------------------------------------------------

st.markdown("""
<style>
.hero {
    padding: 2rem 2rem 2.2rem 2rem;
    border-radius: 1.2rem;
    background: linear-gradient(135deg, #f7fbff 0%, #eef6f9 100%);
    border: 1px solid #d9e6ea;
    margin-bottom: 2rem;
}
.hero-title {
    font-size: 3.2rem;
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 0.4rem;
}
.hero-subtitle {
    font-size: 1.35rem;
    color: #374151;
    margin-bottom: 1.2rem;
}
.hero-text {
    font-size: 1.05rem;
    color: #374151;
    line-height: 1.6;
}
.badge {
    display: inline-block;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    margin-right: 0.4rem;
    margin-top: 0.5rem;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

left, right = st.columns([1.1, 2.2], vertical_alignment="center")

with left:
    if book_cover.exists():
        st.image(str(book_cover), use_container_width=True)
    else:
        st.markdown("## 📊")

with right:
    st.markdown("""
    <div class="hero">
        <div class="hero-title">Health Data Literacy Coach</div>
        <div class="hero-subtitle">
            Helping NHS decision-makers find the right concepts at the right time.
        </div>
        <div class="hero-text">
            Describe the dashboard, pathway, scheme, population question or analytical challenge
            you are working on. The coach will recommend relevant modules from the
            <strong>Health Data Literacy</strong> programme and suggest better questions to ask.
            <br><br>
            <strong>No AI. No patient data. No external data connection.</strong>
        </div>
        <br>
        <span class="badge">📚 Module recommender</span>
        <span class="badge">❓ Suggested questions</span>
        <span class="badge">🧭 Learning pathways</span>
        <span class="badge">🔒 Public-safe prototype</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### What are you trying to understand today?")

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

                with st.expander(module["title"], expanded=True):

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
