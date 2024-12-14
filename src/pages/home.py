"""
MarkItDown Web - Main application page
"""
import streamlit as st
from pathlib import Path
import tempfile
import json
import requests
from streamlit_lottie import st_lottie

from src.utils.converters import MarkdownConverter
from src.utils.file_handlers import cleanup_temp_files, ensure_directories
from src.components.file_uploader import file_uploader_component

# Configure Streamlit page
st.set_page_config(
    page_title="MarkItDown Web",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_lottie_url(url: str):
    """Load Lottie animation from URL"""
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_upload = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_u25cckyh.json")
lottie_convert = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_EyJRpT.json")
lottie_success = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_jmejybvu.json")

# Custom CSS
st.markdown("""
<style>
    /* Modern interactive theme */
    .stApp {
        background: #1a1a1a;
        color: #ffffff;
    }
    
    /* Glowing effects */
    @keyframes glow {
        0% { box-shadow: 0 0 5px #4a90e2; }
        50% { box-shadow: 0 0 20px #4a90e2; }
        100% { box-shadow: 0 0 5px #4a90e2; }
    }
    
    /* Interactive elements */
    .stButton button {
        background: linear-gradient(45deg, #4a90e2, #357abd);
        border: none !important;
        color: white !important;
        padding: 0.5rem 2rem !important;
        border-radius: 25px !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        animation: glow 2s infinite;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        filter: brightness(1.2);
    }
    
    /* Upload zone */
    .uploadfile {
        background: rgba(74, 144, 226, 0.1) !important;
        border: 2px solid #4a90e2 !important;
        border-radius: 15px !important;
        padding: 2rem !important;
        transition: all 0.3s ease !important;
    }
    .uploadfile:hover {
        background: rgba(74, 144, 226, 0.2) !important;
        animation: glow 2s infinite;
    }
    
    /* Cards */
    .info-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    .info-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.1);
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
    if 'show_success' not in st.session_state:
        st.session_state.show_success = False

def show_result(result):
    """Display conversion result"""
    if result.success:
        # Show success animation
        st.session_state.show_success = True
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st_lottie(lottie_success, height=200, key="success")
        
        st.success("✨ Conversion completed successfully!")
        
        # Center-align container for the download button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Large centered download button
            st.download_button(
                label="⬇️ Download Markdown",
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
                <pre style="background: rgba(0,0,0,0.2); padding: 1rem; border-radius: 10px;">
                {result.content}
                </pre>
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
        st.error(f"❌ Conversion failed: {result.error}")

def show_conversion_history():
    """Display conversion history"""
    if st.session_state.conversion_history:
        st.markdown(
            """
            <div class="info-card">
                <h3>📚 Recent Conversions</h3>
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
    
    # Main content
    st.title("📝 MarkItDown Web")
    
    # Show upload animation if no file is being processed
    if not st.session_state.show_success:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st_lottie(lottie_upload, height=200, key="upload")
    
    st.markdown(
        """
        <div style='text-align: center; padding: 1rem 0;'>
            <p style='font-size: 1.2rem; color: #4a90e2;'>
                Transform your documents into clean, readable Markdown.<br>
                Just drop your file and watch the magic happen! ✨
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create centered container
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # File uploader
        file_uploaded, temp_file = file_uploader_component(st.session_state.temp_dir)
    
    # Process file if uploaded
    if file_uploaded and temp_file:
        # Show converting animation
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st_lottie(lottie_convert, height=200, key="converting")
        
        with st.spinner("🔄 Converting your file..."):
            result = st.session_state.converter.convert_file(temp_file)
            show_result(result)
    else:
        st.session_state.show_success = False
    
    # Show conversion history
    show_conversion_history()
    
    # Cleanup temporary files when session ends
    cleanup_temp_files(st.session_state.temp_dir)

if __name__ == "__main__":
    main() 