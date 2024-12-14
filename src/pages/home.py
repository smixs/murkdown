"""
MurDown - Your Markdown Cat Assistant
"""
import streamlit as st
from pathlib import Path
import tempfile

from src.utils.converters import MarkdownConverter
from src.utils.file_handlers import cleanup_temp_files, ensure_directories
from src.components.file_uploader import file_uploader_component

# Configure Streamlit page
st.set_page_config(
    page_title="MurDown",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Hide all streamlit elements
st.markdown("""
    <style>
        /* Hide all Streamlit bars and decorations */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stToolbar {visibility: hidden !important;}
        .stDeployButton {display: none !important;}
        .stActionButton {display: none !important;}
        div[data-testid="stToolbar"] {visibility: hidden !important;}
        div[data-testid="stDecoration"] {visibility: hidden !important;}
        div[data-testid="stStatusWidget"] {visibility: hidden !important;}
        div[data-baseweb="tab-list"] {visibility: hidden !important;}
        button[kind="header"] {display: none !important;}
        .stApp header {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
        div[class="stActionButton"] {display: none !important;}
        div[data-testid="stHeader"] {display: none !important;}
        div[data-testid="stAppViewBlockContainer"] {margin-top: -100px !important;}
    </style>
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
    /* Dark theme */
    .stApp {
        background: #1E1E1E;
        color: #E0E0E0;
    }
    
    /* Main container */
    .main-content {
        background: #2D2D2D;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        margin-top: -100px;  /* Compensate for hidden header */
    }
    
    /* Cat mascot container */
    .cat-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    .cat-container h1 {
        font-size: 3rem;
        margin: 0;
        background: linear-gradient(45deg, #9B6BFF, #FF69B4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    .cat-container p {
        color: #B0B0B0;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Large dropzone */
    .uploadfile {
        background: #363636 !important;
        border: 3px dashed #9B6BFF !important;
        border-radius: 20px !important;
        padding: 4rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        min-height: 300px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: #B0B0B0 !important;
    }
    .uploadfile:hover {
        background: #404040 !important;
        border-color: #FF69B4 !important;
        color: #FFFFFF !important;
    }
    
    /* Download button */
    .stDownloadButton button {
        background: linear-gradient(45deg, #9B6BFF, #FF69B4) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 30px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin: 1rem 0 !important;
    }
    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(155, 107, 255, 0.3);
    }
    
    /* Cards */
    .info-card {
        background: #363636;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #404040;
    }
    
    /* Content area */
    pre {
        background: #2D2D2D !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        border: 1px solid #404040 !important;
        color: #E0E0E0 !important;
    }
    
    /* Success message */
    .stSuccess {
        background: rgba(155, 107, 255, 0.2) !important;
        color: #FFFFFF !important;
    }
    
    /* Error message */
    .stError {
        background: rgba(255, 105, 180, 0.2) !important;
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'converter' not in st.session_state:
        st.session_state.converter = MarkdownConverter()
    if 'temp_dir' not in st.session_state:
        st.session_state.temp_dir = Path(tempfile.mkdtemp())
    if 'conversion_history' not in st.session_state:
        st.session_state.conversion_history = []

def show_result(result):
    """Display conversion result"""
    if result.success:
        st.success("😺 Purrfect! Your file has been converted!")
        
        # Center-align container for the download button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Large centered download button
            st.download_button(
                label="🐾 Download Markdown",
                data=result.content,
                file_name=Path(result.output_file).name,
                mime="text/markdown",
                use_container_width=True,
            )
        
        # Show full content in a card
        st.markdown(
            f"""
            <div class="info-card">
                <h3>📄 Converted Content</h3>
                <pre>{result.content}</pre>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add to history
        if len(st.session_state.conversion_history) >= 5:
            st.session_state.conversion_history.pop(0)
        st.session_state.conversion_history.append({
            'input': result.original_file,
            'output': result.output_file,
            'timestamp': st.session_state.get('timestamp', 'Unknown')
        })
    else:
        st.error(f"😿 Oops! Something went wrong: {result.error}")

def show_conversion_history():
    """Display conversion history"""
    if st.session_state.conversion_history:
        st.markdown(
            """
            <div class="info-card">
                <h3>🐱 Recent Adventures</h3>
            """,
            unsafe_allow_html=True
        )
        for item in reversed(st.session_state.conversion_history):
            st.markdown(f"- 📄 {Path(item['input']).name} → {Path(item['output']).name}")
        st.markdown("</div>", unsafe_allow_html=True)

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Main content container
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Cat mascot header
    st.markdown(
        """
        <div class="cat-container">
            <h1>MurDown</h1>
            <p>Your purr-fessional Markdown conversion companion! 🐱</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style='text-align: center; padding: 1rem 0;'>
            <p style='font-size: 1.2rem; color: #B0B0B0;'>
                Drop your documents here and let MurDown work his magic!<br>
                He'll turn them into purrfect Markdown in no time. 🐾
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create centered container for file uploader
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        # File uploader
        file_uploaded, temp_file = file_uploader_component(st.session_state.temp_dir)
    
    # Process file if uploaded
    if file_uploaded and temp_file:
        with st.spinner("🔄 Converting your file..."):
            result = st.session_state.converter.convert_file(temp_file)
            show_result(result)
    
    # Show conversion history
    show_conversion_history()
    
    # Close main content container
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Cleanup temporary files when session ends
    cleanup_temp_files(st.session_state.temp_dir)

if __name__ == "__main__":
    main() 