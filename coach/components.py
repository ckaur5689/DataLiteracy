import streamlit as st


def hero(book_cover):

    left, right = st.columns([1.1,2.2])

    with left:

        st.image(str(book_cover), use_container_width=True)

    with right:

        st.markdown("""
        <div class="hero">

        <div class="hero-title">
        Health Data Literacy Coach
        </div>

        <div class="hero-subtitle">
        Your interactive companion to the Health Data Literacy programme
        </div>

        <div class="hero-text">

        Helping NHS decision-makers ask better questions,
        interpret data confidently,
        and navigate the right learning module
        at the point they need it.

        <br><br>

        <b>No AI. No patient data. Just better questions and better decisions.</b>

        <br><br>

        <span class="badge">📚 Module Recommender</span>

        <span class="badge">❓ Better Questions</span>

        <span class="badge">🧭 Learning Pathways</span>

        </div>

        </div>
        """, unsafe_allow_html=True)


def module_card(module):

    st.markdown('<div class="module-card">', unsafe_allow_html=True)

    st.markdown(f"## 📘 {module['title']}")

    st.markdown(
        f'<span class="pathway">{module["pathway"]}</span>',
        unsafe_allow_html=True
    )

    st.markdown("### Why this module?")

    for keyword in module["matched_keywords"]:

        st.markdown(
            f'<span class="keyword">{keyword}</span>',
            unsafe_allow_html=True
        )

    st.markdown("### Questions")

    for question in module["questions"]:

        st.markdown(f"- {question}")

    st.link_button(
        "📖 Open Module",
        module["module_url"]
    )

    st.markdown("</div>", unsafe_allow_html=True)
