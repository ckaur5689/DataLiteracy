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

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="top-panel">

    <h1 class="hero-title">
    Health Data Literacy Companion
    </h1>

    <p class="hero-subtitle">
    Helping healthcare leaders ask better questions.
    </p>

    <div class="hero-badge">
    📘 Based on the Health Data Literacy Programme
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    if book_cover.exists():
        st.markdown('<div style="margin-top: 10px;">', unsafe_allow_html=True)
        st.image(book_cover, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Book cover image not found.")

st.markdown(
    "<p style='text-align:center; color:#6B7280; font-weight:700;'>"
    "What challenge are you facing today?"
    "</p>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#6B7280;'>"
    "Choose a common healthcare analytics challenge below, or describe your own."
    "</p>",
    unsafe_allow_html=True
)

# ------------------------------------------------------
# Challenge questions
# ------------------------------------------------------

challenge_questions = {
    "Dashboard Interpretation": [
        "I am reviewing a dashboard and I am not sure whether the trend is meaningful.",
        "Performance has deteriorated this month. Should I be concerned?",
        "The dashboard shows a red RAG rating. Does that necessarily mean performance is poor?",
        "Are we looking at normal variation or a genuine change?",
        "What questions should I ask before acting on this dashboard?"
    ],

    "Evaluation & Evidence": [
        "We introduced a frailty pathway and admissions appear lower. Has it worked?",
        "How can we tell whether a new service has made a difference?",
        "What evidence do we need before expanding a pilot?",
        "Could the apparent improvement have happened anyway?",
        "Which evaluation method would be most appropriate?"
    ],

    "Comparing Populations": [
        "We want to compare performance between places with different populations.",
        "Should we adjust for age or deprivation before comparing outcomes?",
        "Are these organisations genuinely comparable?",
        "Could differences in case mix explain the variation in performance?",
        "Should we use counts, rates or standardised measures?"
    ],

    "Risk, Probability & Uncertainty": [
        "What level of uncertainty exists in this analysis?",
        "How much confidence should we place in this estimate?",
        "Is this an absolute risk or a relative risk?",
        "What are the consequences of a false positive or false negative?",
        "How should uncertainty influence the decision?"
    ],

    "Demand & Capacity": [
        "We are trying to understand demand, capacity and flow across a pathway.",
        "Why is the waiting list growing even though activity has increased?",
        "Where is the main bottleneck in the pathway?",
        "Do we have a demand problem, a capacity problem or a flow problem?",
        "Why are waiting times increasing despite more outpatient appointments?"
    ],

    "Health Economics": [
        "I want to know whether a pilot scheme delivered value for money.",
        "Is this intervention cost-effective?",
        "What is the opportunity cost of investing in this service?",
        "Are the financial benefits occurring in a different part of the system?",
        "Which health economic evaluation method should we use?"
    ]
}


# ------------------------------------------------------
# Session state
# ------------------------------------------------------

if "selected_challenge" not in st.session_state:
    st.session_state.selected_challenge = None

if "question_text" not in st.session_state:
    st.session_state.question_text = ""


def select_challenge(challenge_name):
    """Select a challenge and populate the text area with its first question."""
    st.session_state.selected_challenge = challenge_name
    st.session_state.question_text = challenge_questions[challenge_name][0]


def update_question_from_dropdown(dropdown_key):
    """Copy the selected example question into the editable text area."""
    selected_value = st.session_state[dropdown_key]

    if selected_value == "Write my own question":
        st.session_state.question_text = ""
    elif selected_value != "Choose a question":
        st.session_state.question_text = selected_value


# ------------------------------------------------------
# Challenge cards
# ------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "📊\n\nDashboard Interpretation",
        key="dashboard_card",
        use_container_width=True,
        on_click=select_challenge,
        args=("Dashboard Interpretation",)
    )

with col2:
    st.button(
        "🧪\n\nEvaluation & Evidence",
        key="evaluation_card",
        use_container_width=True,
        on_click=select_challenge,
        args=("Evaluation & Evidence",)
    )

with col3:
    st.button(
        "👥\n\nComparing Populations",
        key="population_card",
        use_container_width=True,
        on_click=select_challenge,
        args=("Comparing Populations",)
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "🎯\n\nRisk, Probability & Uncertainty",
        key="risk_card",
        use_container_width=True,
        on_click=select_challenge,
        args=("Risk, Probability & Uncertainty",)
    )

with col2:
    st.button(
        "🏥\n\nDemand & Capacity",
        key="capacity_card",
        use_container_width=True,
        on_click=select_challenge,
        args=("Demand & Capacity",)
    )

with col3:
    st.button(
        "💷\n\nHealth Economics",
        key="economics_card",
        use_container_width=True,
        on_click=select_challenge,
        args=("Health Economics",)
    )


# ------------------------------------------------------
# Example-question dropdown
# ------------------------------------------------------

if st.session_state.selected_challenge:

    selected_challenge = st.session_state.selected_challenge

    st.markdown(
        f"### {selected_challenge}"
    )

    st.markdown(
        "Choose a common question, or write your own below."
    )

    dropdown_key = (
        "question_choice_"
        + selected_challenge.lower().replace(" ", "_").replace("&", "and")
    )

    question_options = (
        ["Choose a question"]
        + challenge_questions[selected_challenge]
        + ["Write my own question"]
    )

    st.selectbox(
        "Useful starting questions",
        options=question_options,
        key=dropdown_key,
        on_change=update_question_from_dropdown,
        args=(dropdown_key,)
    )

else:
    st.info(
        "Choose one of the challenge areas above, or describe your own question below."
    )


# ------------------------------------------------------
# Editable question
# ------------------------------------------------------

st.markdown(
    """
    <p style="
        text-align:center;
        color:#374151;
        font-weight:700;
        font-size:1.2rem;
    ">
        Or describe your own challenge
    </p>
    """,
    unsafe_allow_html=True
)

user_input = st.text_area(
    "Describe your challenge in your own words",
    key="question_text",
    height=140,
    placeholder=(
        "For example: We introduced a frailty pathway and admissions "
        "have fallen. Has it actually made a difference?"
    )
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
        "🔍 Recommend Learning Modules",
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

st.markdown(
    """
    <h2 style="
        color:#1F2937;
        font-weight:700;
        margin-top:20px;
        margin-bottom:15px;
    ">
        📚 Browse Module Library
    </h2>
    """,
    unsafe_allow_html=True
)

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
