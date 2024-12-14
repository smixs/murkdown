"""
File uploader component for Streamlit interface
"""
import streamlit as st
from pathlib import Path
from typing import Optional, Tuple
from src.utils.converters import MarkdownConverter, SUPPORTED_FORMATS
from src.utils.file_handlers import save_uploaded_file, get_file_size

def file_uploader_component(temp_dir: Path) -> Tuple[bool, Optional[Path]]:
    """
    Display file uploader component
    
    Args:
        temp_dir: Directory for temporary files
        
    Returns:
        Tuple of (file_uploaded, file_path)
    """
    # File uploader
    st.markdown("### Upload File")
    uploaded_file = st.file_uploader(
        "Choose a file to convert",
        type=list(SUPPORTED_FORMATS.keys()),
        help="Select a file to convert to Markdown format",
        key="file_uploader"
    )
    
    if uploaded_file is not None:
        # Show file info
        st.markdown("#### File Details")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Name:** {uploaded_file.name}")
        with col2:
            st.markdown(f"**Size:** {len(uploaded_file.getvalue()) / 1024:.1f} KB")
        
        # Save file
        temp_file = save_uploaded_file(uploaded_file, temp_dir)
        if temp_file:
            return True, temp_file
        else:
            st.error("Failed to save uploaded file")
    
    return False, None
