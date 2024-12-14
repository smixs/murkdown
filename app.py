import streamlit as st
from src.pages.home import main

# Базовая конфигурация приложения
st.set_page_config(
    page_title="MurkDown - Purrfect for LLMs 🐱",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Глобальные настройки стиля
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .uploadedFile {
        border: 2px dashed #cccccc;
        border-radius: 5px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
    }
    .murk {
        color: #FF69B4;
    }
    .cat-container {
        text-align: center;
        padding: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Инициализация состояния сессии
if 'converted_files' not in st.session_state:
    st.session_state['converted_files'] = []
if 'current_file' not in st.session_state:
    st.session_state['current_file'] = None

if __name__ == "__main__":
    main() 