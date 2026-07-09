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

    .hero-title{
    
        color:white;
    
        font-size:3.3rem;
    
        font-weight:700;
    
        margin-bottom:10px;
    
    }

    .hero-subtitle{
    
        color:#EAF4FF;
    
        font-size:1.4rem;
    
        margin-bottom:25px;
    
    }

    .hero-text {
        color: white;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .hero-badge{
    
        display:inline-block;
    
        background:rgba(255,255,255,.18);
    
        color:white;
    
        border-radius:999px;
    
        padding:12px 22px;
    
        border:1px solid rgba(255,255,255,.35);
    
        font-size:1rem;
    
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

    .top-panel {
    
        background: linear-gradient(135deg,#005EB8,#2F80D1);
    
        border-radius:24px;
    
        padding:50px;
    
        margin-bottom:40px;
    
        text-align:center;
    
        box-shadow:0 10px 25px rgba(0,0,0,.12);
    
    }
    .stButton > button {
        border-radius: 16px;
        height: 145px;
        font-size: 18px;
        font-weight: 700;
        border: 1px solid #C7D7EA;
        background: white;
        color: #1F2937;
        transition: .2s;
    }
    
    .stButton > button:hover {
        border-color: #005EB8;
        color: #005EB8;
        box-shadow: 0 6px 18px rgba(0,94,184,.25);
        transform: translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)
