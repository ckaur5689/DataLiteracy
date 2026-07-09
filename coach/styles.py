import streamlit as st

NHS_BLUE = "#005EB8"
NHS_BLUE_LIGHT = "#2F80D1"

ACTION_GREEN = "#198754"
ACTION_GREEN_DARK = "#157347"

BACKGROUND = "#FFFFFF"

LIGHT_GREY = "#F8F9FA"

TEXT = "#1F2937"

BORDER = "#D9E2EC"

def load_css():
    st.markdown("""
    <style>

    .stApp {
        background-color: #FFFFFF;
    }

    .hero {
        background: linear-gradient(135deg, #0B5CAB, #3A8DDE);
        color: #F8FAFC;
        border-radius: 25px;
        padding: 35px;
        margin-bottom: 30px;
        box-shadow: 0 8px 25px rgba(0,0,0,.12);
    }
    
    .hero-title {
        color: #F8FAFC;
        font-size: 2.8rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,.15);
    }

    .hero-subtitle{
    
        color:#EAF4FF;
    
        font-size:1.4rem;
    
        margin-bottom:25px;
    
    }

    .hero-text {
        color: #F8FAFC;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .hero-badge{
    
        display:inline-block;
    
        background:rgba(255,255,255,.18);
    
        color:#F8FAFC;
    
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
    
        border-radius:18px;
    
        padding:30px;
    
        margin-bottom:40px;
    
        text-align:center;
    
        box-shadow:0 10px 25px rgba(0,0,0,.12);
    
    }

  .stTextArea textarea {

    background-color: #F7FBFF !important;

    border: 2px solid #BFD7EA !important;

    border-radius: 12px !important;

    }
    
    .stButton > button {
    
        background: linear-gradient(135deg, #005EB8, #1976D2);
    
        color: #F8FAFC;
    
        border: none;
    
        border-radius: 18px;
    
        height: 145px;
    
        font-size: 18px;
    
        font-weight: 700;
    
        padding: 20px;
    
        box-shadow: 0 6px 16px rgba(0,94,184,.25);
    
        transition: all 0.2s ease;
    
    }
 /* -------------------------------------------------- */
 /* Primary button (Recommend My Learning Path)        */
 /* -------------------------------------------------- */

    button[kind="primary"] {
    
        background: #198754 !important;
    
        color: white !important;
    
        border: none !important;
    
        border-radius: 12px !important;
    
        height: 60px !important;
    
        font-size: 20px !important;
    
        font-weight: 700 !important;
    
        box-shadow: 0 4px 12px rgba(25,135,84,.30);
    
    }

    button[kind="primary"]:hover {
    
        background: #157347 !important;
    
        color: white !important;

    }
    
    .stButton > button:hover {
    
        background: linear-gradient(135deg, #004B93, #1565C0);
    
        color: #F8FAFC;
    
        transform: translateY(-3px);
    
        box-shadow: 0 10px 22px rgba(0,94,184,.35);
    
    }

    .stButton > button:active {

    transform: translateY(1px);

    }

    .stButton > button {

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    }
    </style>
    """, unsafe_allow_html=True)
