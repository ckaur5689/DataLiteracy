import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* ==================================================
           PAGE
        ================================================== */

        .stApp {
            background-color: #FFFFFF;
            color: #1F2937;
        }

        .block-container {
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .stMarkdown h1,
        .stMarkdown h2,
        .stMarkdown h3,
        .stMarkdown h4 {
            color: #1F2937;
        }

        .stMarkdown p,
        .stMarkdown li {
            color: #374151;
        }


        /* ==================================================
           LANDING PANEL
        ================================================== */

        .top-panel {
            background: linear-gradient(135deg, #005EB8, #2F80D1);
            border-radius: 18px;
            padding: 15px 30px;
            margin-top: 15px;
            margin-bottom: 20px;
            text-align: center;
            box-shadow: 0 8px 22px rgba(0, 0, 0, 0.12);
        }

        .hero-title {
            color: #F8FAFC !important;
            font-size: 2rem;
            font-weight: 700;
            line-height: 1.1;
            margin-top: 0;
            margin-bottom: 0.25rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
        }

        .hero-subtitle {
            color: rgba(255, 255, 255, 0.94) !important;
            font-size: 1.05rem;
            font-weight: 400;
            line-height: 1.5;
            margin-bottom: 10px;
        }

        .hero-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.12);
            color: #FFFFFF;
            border: 1px solid rgba(255, 255, 255, 0.30);
            border-radius: 999px;
            padding: 8px 16px;
            font-size: 0.9rem;
        }


        /* ==================================================
           CHALLENGE BUTTONS
        ================================================== */

        .stButton > button {
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;

            width: 100%;
            min-height: 85px;
            height: auto;
            padding: 14px 10px;

            background: #2F80D1;
            color: #FFFFFF;

            border: none;
            border-radius: 14px;

            font-size: 16px;
            font-weight: 700;
            line-height: 1.35;

            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.10);
            transition: all 0.2s ease;
        }

         .stButton > button:hover {
        
            background:#5A9FE3;
        
            color:white;
        
            border:3px solid white;
        
            outline:3px solid #005EB8;
        
            transform:translateY(-3px) scale(1.02);
        
            box-shadow:0 10px 20px rgba(0,94,184,.25);
        
        }

        .stButton > button:active {
            transform: translateY(1px);
        }


        /* ==================================================
           PRIMARY BUTTON — RECOMMEND MY LEARNING PATH
        ================================================== */

        button[kind="primary"],
        div[data-testid="stBaseButton-primary"] > button {
            background: #198754 !important;
            color: #FFFFFF !important;

            min-height: 56px !important;
            height: auto !important;
            padding: 12px 18px !important;

            border: none !important;
            border-radius: 12px !important;

            font-size: 18px !important;
            font-weight: 700 !important;

            box-shadow: 0 4px 12px rgba(25, 135, 84, 0.25) !important;
            transform: none !important;
        }

        button[kind="primary"]:hover,
        div[data-testid="stBaseButton-primary"] > button:hover {
            background: #157347 !important;
            color: #FFFFFF !important;
        
            border: 2px solid #FFFFFF !important;
        
            transform: translateY(-2px) scale(1.01) !important;
        
            box-shadow:
                0 0 0 2px #198754,
                0 8px 18px rgba(25,135,84,.35) !important;
        
            transition: all 0.2s ease;
        }

       button[kind="primary"]:active,
       div[data-testid="stBaseButton-primary"] > button:active {
        
            border: 2px solid #FFFFFF !important;
        
            background: #146C43 !important;
        
            transform: translateY(1px) !important;
        
        }
    


        /* ==================================================
           TEXT AREA
        ================================================== */

        .stTextArea label,
        .stTextArea label p {
            color: #1F2937 !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
        }

        .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #1F2937 !important;

            border: 2px solid #BFD7EA !important;
            border-radius: 12px !important;

            padding: 14px !important;
            font-size: 16px !important;
            line-height: 1.5 !important;
        }

        .stTextArea textarea:focus {
            border-color: #005EB8 !important;
            box-shadow: 0 0 0 4px rgba(0, 94, 184, 0.14) !important;
            outline: none !important;
        }

        .stTextArea textarea::placeholder {
            color: #6B7280 !important;
            opacity: 1 !important;
        }


        /* ==================================================
           RECOMMENDED MODULE CARDS
        ================================================== */

        .module-card {
            background: #FFFFFF;
            border: 1px solid #D9E2EC;
            border-left: 6px solid #005EB8;
            border-radius: 14px;

            padding: 24px;
            margin-bottom: 18px;

            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.07);
        }

        .module-card h2,
        .module-card h3,
        .module-card p,
        .module-card li {
            color: #1F2937 !important;
        }

        .pathway {
            display: inline-block;
            background: #005EB8;
            color: #FFFFFF;

            padding: 5px 10px;
            margin-bottom: 12px;

            border-radius: 15px;
            font-size: 0.8rem;
        }

        .keyword {
            display: inline-block;
            background: #EAF4FF;
            color: #003087;

            padding: 4px 10px;
            margin: 3px;

            border-radius: 15px;
            font-size: 0.8rem;
        }


        /* ==================================================
           MODULE LIBRARY EXPANDERS
        ================================================== */

        div[data-testid="stExpander"] {
            background-color: #FFFFFF !important;
            border: 1px solid #C9D4E0 !important;
            border-radius: 12px !important;

            margin-bottom: 14px !important;
            overflow: hidden !important;
        }

        div[data-testid="stExpander"] summary {
            background-color: #FFFFFF !important;
            color: #1F2937 !important;

            min-height: 58px !important;
            padding: 14px 16px !important;
        }

        div[data-testid="stExpander"] summary p {
            color: #1F2937 !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            line-height: 1.4 !important;
        }

        div[data-testid="stExpander"] summary svg {
            fill: #005EB8 !important;
            color: #005EB8 !important;
        }

        div[data-testid="stExpander"]
        div[data-testid="stMarkdownContainer"],
        div[data-testid="stExpander"]
        div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stExpander"]
        div[data-testid="stMarkdownContainer"] li,
        div[data-testid="stExpander"]
        div[data-testid="stMarkdownContainer"] strong {
            color: #1F2937 !important;
        }


        /* ==================================================
           LEARNING PATHWAY SELECTBOX
        ================================================== */

        div[data-testid="stSelectbox"] label,
        div[data-testid="stSelectbox"] label p {
            color: #1F2937 !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
        }

        div[data-testid="stSelectbox"]
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            color: #1F2937 !important;

            border: 1px solid #9FB6CC !important;
            border-radius: 10px !important;
            min-height: 50px !important;
        }

        div[data-testid="stSelectbox"]
        div[data-baseweb="select"] span {
            color: #1F2937 !important;
        }


        /* ==================================================
           OPEN MODULE LINK BUTTONS
        ================================================== */

        div[data-testid="stLinkButton"] a {
            background-color: #198754 !important;
            color: #FFFFFF !important;

            border: none !important;
            border-radius: 10px !important;

            font-weight: 700 !important;
        }

        div[data-testid="stLinkButton"] a:hover {
            background-color: #157347 !important;
            color: #FFFFFF !important;
        }


        /* ==================================================
           MOBILE
        ================================================== */

        @media (max-width: 768px) {

            .block-container {
                padding-top: 1.25rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                padding-bottom: 2rem !important;
            }

            .top-panel {
                padding: 24px 16px !important;
                margin-bottom: 24px !important;
                border-radius: 16px !important;
            }

            .hero-title {
                font-size: 2rem !important;
                line-height: 1.2 !important;
            }

            .hero-subtitle {
                font-size: 1rem !important;
                line-height: 1.5 !important;
                margin-bottom: 16px !important;
            }

            .hero-badge {
                padding: 8px 12px !important;
                font-size: 0.86rem !important;
                line-height: 1.4 !important;
            }

            .stMarkdown h2 {
                color: #1F2937 !important;
                font-size: 1.7rem !important;
                line-height: 1.25 !important;
            }

            .stMarkdown h3 {
                color: #1F2937 !important;
                font-size: 1.25rem !important;
                line-height: 1.35 !important;
            }

            .stMarkdown p {
                color: #374151 !important;
                font-size: 1rem !important;
                line-height: 1.6 !important;
            }

            .stButton > button {
                min-height: 72px !important;
                height: auto !important;
                padding: 11px 8px !important;
                font-size: 15px !important;
            }

            button[kind="primary"],
            div[data-testid="stBaseButton-primary"] > button {
                min-height: 54px !important;
                height: auto !important;
                padding: 12px !important;
                font-size: 16px !important;
            }

            .stTextArea textarea {
                min-height: 130px !important;
                background-color: #FFFFFF !important;
                color: #1F2937 !important;
                font-size: 16px !important;
            }

            div[data-testid="stExpander"] summary {
                min-height: 62px !important;
                padding: 15px 13px !important;
            }

            div[data-testid="stExpander"] summary p {
                color: #1F2937 !important;
                font-size: 1.02rem !important;
                line-height: 1.45 !important;
            }

            div[data-testid="stExpander"]
            div[data-testid="stMarkdownContainer"] p,
            div[data-testid="stExpander"]
            div[data-testid="stMarkdownContainer"] li,
            div[data-testid="stExpander"]
            div[data-testid="stMarkdownContainer"] strong {
                color: #1F2937 !important;
                font-size: 1rem !important;
                line-height: 1.65 !important;
            }

            div[data-testid="stLinkButton"] a {
                width: 100% !important;
                min-height: 48px !important;
                justify-content: center !important;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
