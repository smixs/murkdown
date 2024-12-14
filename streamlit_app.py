"""
MurDown - Your Markdown Cat Assistant
"""
import streamlit as st
from pathlib import Path
import tempfile
import base64

from src.utils.converters import MarkdownConverter
from src.utils.file_handlers import cleanup_temp_files, ensure_directories
from src.components.file_uploader import file_uploader_component

# Configure Streamlit page
st.set_page_config(
    page_title="MurDown",
    page_icon="🐱",
    layout="centered"
)

# Initialize session state
if 'converted_files' not in st.session_state:
    st.session_state['converted_files'] = []
if 'current_file' not in st.session_state:
    st.session_state['current_file'] = None

def initialize_session_state():
    """Initialize session state variables"""
    if 'converter' not in st.session_state:
        st.session_state.converter = MarkdownConverter()
    if 'temp_dir' not in st.session_state:
        st.session_state.temp_dir = Path(tempfile.mkdtemp())
    if 'conversion_history' not in st.session_state:
        st.session_state.conversion_history = []

def main():
    initialize_session_state()
    
    # Header with cat mascot
    st.markdown("""
    <div class="cat-container">
        <h1><span class="murk">Mur</span><span>Down</span></h1>
        <p>Your Markdown Cat Assistant</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content will be handled by the pages

if __name__ == "__main__":
    main() 