import streamlit as st


def load_css():

    st.markdown("""
    <style>

    .hero {
        padding:2rem;
        border-radius:18px;
        background:linear-gradient(135deg,#f7fbff,#eef6f9);
        border:1px solid #d8e3ea;
        margin-bottom:2rem;
    }

    .hero-title{
        font-size:3rem;
        font-weight:700;
        margin-bottom:0.2rem;
    }

    .hero-subtitle{
        font-size:1.3rem;
        color:#4b5563;
        margin-bottom:1rem;
    }

    .hero-text{
        font-size:1.05rem;
        line-height:1.6;
        color:#374151;
    }

    .badge{
        display:inline-block;
        background:#0f766e;
        color:white;
        padding:6px 12px;
        margin:4px;
        border-radius:20px;
        font-size:0.85rem;
    }

    .module-card{

        background:white;
        border-radius:15px;
        padding:20px;
        margin-bottom:20px;
        border:1px solid #e5e7eb;
        box-shadow:0 2px 8px rgba(0,0,0,.08);

    }

    .pathway{

        display:inline-block;
        background:#2563eb;
        color:white;
        padding:5px 10px;
        border-radius:15px;
        font-size:0.8rem;
        margin-bottom:12px;

    }

    .keyword{

        display:inline-block;
        background:#eef6ff;
        color:#003366;
        border-radius:15px;
        padding:4px 10px;
        margin:3px;
        font-size:0.8rem;

    }

    .stButton > button {
    height: 130px;
    border-radius: 15px;
    font-size: 18px;
    font-weight: 600;
   }

    </style>
    """, unsafe_allow_html=True)
