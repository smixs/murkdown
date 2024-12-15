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
    # Initialize session state for tracking last uploaded file
    if 'last_uploaded_file' not in st.session_state:
        st.session_state.last_uploaded_file = None
    
    # File uploader with custom styling
    uploaded_file = st.file_uploader(
        "🐱 Drop your file here for MurDowd to process",
        type=list(SUPPORTED_FORMATS.keys()),
        help="MurDowd can handle various file types and convert them to Markdown",
        key="file_uploader",
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        # Check if this is a new file
        if st.session_state.last_uploaded_file != uploaded_file.name:
            st.session_state.last_uploaded_file = uploaded_file.name
            # Reset conversion states for new file
            st.session_state.conversion_result = None
            st.session_state.is_converting = False
            
        # Save file
        temp_file = save_uploaded_file(uploaded_file, temp_dir)
        if temp_file:
            return True, temp_file
        else:
            st.error("😿 MurDowd couldn't save the file")
    
    return False, None
