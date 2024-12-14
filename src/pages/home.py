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
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* Dark theme */
    .stApp {
        background: #1E1E1E;
        color: #E0E0E0;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Cat mascot container */
    .cat-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    .cat-container h1 {
        font-size: 3rem;
        margin: 0;
        font-weight: 700;
        font-family: 'Space Grotesk', sans-serif;
        color: #00A4FF;
    }
    .cat-container h1 span.murk {
        color: #FF2261;
    }
    .cat-container h1 span:last-child {
        color: #00A4FF;
    }
    .cat-container p {
        color: #B0B0B0;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Large dropzone */
    div[data-testid="stFileUploader"] {
        width: 100% !important;
    }
    
    /* Hide Browse Files button */
    div[data-testid="stFileUploader"] button[kind="secondary"] {
        display: none !important;
    }
    
    div[data-testid="stFileUploader"] > section {
        padding: 0 !important;
        background: transparent !important;
    }
    
    div[data-testid="stFileUploader"] > section > div {
        background: #2D2D2D !important;
        border: 3px dashed #FF2261 !important;
        border-radius: 20px !important;
        padding: 2rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        height: 300px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        color: #B0B0B0 !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 16px !important;
        font-weight: 400 !important;
        line-height: 1.6 !important;
        cursor: pointer !important;
        -webkit-font-smoothing: auto !important;
        background-clip: padding-box !important;
    }
    
    div[data-testid="stFileUploader"] > section > div:hover {
        background: #363636 !important;
        border-color: #00A4FF !important;
        color: #FFFFFF !important;
    }
    
    div[data-testid="stFileUploader"] p {
        font-size: 16px !important;
        color: #B0B0B0 !important;
    }
    
    div[data-testid="stFileUploader"] small {
        font-size: 14px !important;
        color: #808080 !important;
    }
    
    /* Download button */
    .stDownloadButton button {
        background: #FF2261 !important;
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
        background: #00A4FF !important;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 164, 255, 0.3);
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
        background: rgba(255, 34, 97, 0.2) !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        text-align: center !important;
    }
    
    /* Error message */
    .stError {
        background: rgba(0, 164, 255, 0.2) !important;
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
        # Center-align container for success message
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.success("😺 Purrfect! Your file has been converted!")
        
        # Center-align container for the download button
        col1, col2, col3 = st.columns([1, 3, 1])
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

def get_base64_of_bin_file(file_path: str) -> str:
    with open(file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get cat image as base64
cat_image = get_base64_of_bin_file('static/images/cat.png')

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Cat mascot header
    st.markdown(
        """
        <div class="cat-container">
            <h1><span class="murk">Murk</span>Down</h1>
            <p>Your purr-fessional Markdown conversion companion! 🐱</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Cat image with base64
    st.markdown(
        f"""
        <div style='text-align: center; margin: 2rem 0;'>
            <img src="data:image/png;base64,{cat_image}" 
                 style="width: 300px; height: 300; object-fit: contain;">
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
    
    # Cleanup temporary files when session ends
    cleanup_temp_files(st.session_state.temp_dir)

if __name__ == "__main__":
    main() 