"""
MarkItDown Web - Main application page
"""
import streamlit as st
from pathlib import Path
import tempfile

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
        st.success("Conversion completed successfully!")
        
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
        
        # Show full content below
        st.markdown("### Converted Content")
        st.markdown(result.content)
        
        # Add to history
        if len(st.session_state.conversion_history) >= 5:
            st.session_state.conversion_history.pop(0)
        st.session_state.conversion_history.append({
            'input': result.original_file,
            'output': result.output_file,
            'timestamp': st.session_state.get('timestamp', 'Unknown')
        })
    else:
        st.error(f"Conversion failed: {result.error}")

def show_conversion_history():
    """Display conversion history"""
    if st.session_state.conversion_history:
        st.markdown("### Recent Conversions")
        for item in reversed(st.session_state.conversion_history):
            st.markdown(f"- {Path(item['input']).name} → {Path(item['output']).name}")

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Main content
    st.title("MarkItDown Web")
    st.markdown(
        "Convert your documents, presentations, and other files to Markdown format. "
        "Perfect for content analysis and processing."
    )
    
    # File uploader
    file_uploaded, temp_file = file_uploader_component(st.session_state.temp_dir)
    
    # Process file if uploaded
    if file_uploaded and temp_file:
        with st.spinner("Converting file..."):
            result = st.session_state.converter.convert_file(temp_file)
            show_result(result)
    
    # Show conversion history
    show_conversion_history()
    
    # Cleanup temporary files when session ends
    cleanup_temp_files(st.session_state.temp_dir)

if __name__ == "__main__":
    main() 