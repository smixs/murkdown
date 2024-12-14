"""
MarkItDown Web - Main application page
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
    page_title="MarkItDown Web",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    /* Modern theme */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/yourusername/markitdown/main/static/images/background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #ffffff;
    }
    
    /* Main container */
    .main-content {
        background: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }
    
    /* Large dropzone */
    .uploadfile {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 3px dashed rgba(255, 255, 255, 0.3) !important;
        border-radius: 20px !important;
        padding: 4rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        min-height: 300px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .uploadfile:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        border-color: rgba(255, 255, 255, 0.5) !important;
    }
    
    /* Download button */
    .stDownloadButton button {
        background: linear-gradient(45deg, #4a90e2, #357abd) !important;
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
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Cards */
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    /* Content area */
    pre {
        background: rgba(0, 0, 0, 0.3) !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
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
    
    # Main content container
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    st.title("📝 MarkItDown Web")
    st.markdown(
        """
        <div style='text-align: center; padding: 1rem 0;'>
            <p style='font-size: 1.2rem; opacity: 0.8;'>
                Transform your documents into clean, readable Markdown.<br>
                Just drop your file and we'll handle the rest.
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