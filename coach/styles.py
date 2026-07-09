import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .stApp {
        background-color: #F5F9FC;
    }

    .hero {
        background: linear-gradient(135deg, #005EB8, #1E88E5);
        color: white;
        border-radius: 18px;
        padding: 35px;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(0,0,0,.12);
    }

    .hero-title {
        color: white;
        font-size: 3.2rem;
        font-weight: 700;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #EAF4FF;
        margin-bottom: 1rem;
    }

    .hero-text {
        color: white;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .badge {
        display: inline-block;
        background: rgba(255,255,255,0.18);
        color: white;
        padding: 6px 12px;
        margin: 4px;
        border-radius: 20px;
        font-size: 0.85rem;
        border: 1px solid rgba(255,255,255,0.35);
    }

    .module-card {
        background: white;
        border-left: 6px solid #005EB8;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 5px 15px rgba(0,0,0,.08);
    }

    .pathway {
        display: inline-block;
        background: #005EB8;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        margin-bottom: 12px;
    }

    .keyword {
        display: inline-block;
        background: #EAF4FF;
        color: #003087;
        border-radius: 15px;
        padding: 4px 10px;
        margin: 3px;
        font-size: 0.8rem;
    }

    .stButton > button {
        border-radius: 12px;
        height: 130px;
        font-size: 18px;
        font-weight: 600;
        border: 1px solid #C7D7EA;
        background: white;
        transition: .2s;
    }

    .stButton > button:hover {
        border-color: #005EB8;
        color: #005EB8;
        box-shadow: 0 5px 15px rgba(0,94,184,.25);
    }

    </style>
    """, unsafe_allow_html=True)
