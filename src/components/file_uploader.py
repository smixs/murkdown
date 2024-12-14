"""
File uploader component for Streamlit interface
"""
import streamlit as st
from pathlib import Path
from typing import Optional, Tuple
from src.utils.converters import MarkdownConverter, SUPPORTED_FORMATS
from src.utils.file_handlers import save_uploaded_file, get_file_size

def show_supported_formats():
    """Display supported file formats"""
    st.markdown("### Supported Formats")
    
    # Group formats by type
    format_groups = {
        "Documents": ["pdf", "docx", "pptx", "xlsx"],
        "Images": ["png", "jpg", "jpeg"],
        "Audio": ["mp3", "wav"],
        "Text": ["txt", "html"]
    }
    
    # Create columns for format groups
    cols = st.columns(len(format_groups))
    
    # Display formats by group
    for col, (group, formats) in zip(cols, format_groups.items()):
        with col:
            st.markdown(f"**{group}**")
            for fmt in formats:
                st.markdown(f"- .{fmt}")

def file_uploader_component(temp_dir: Path) -> Tuple[bool, Optional[Path]]:
    """
    Display file uploader component
    
    Args:
        temp_dir: Directory for temporary files
        
    Returns:
        Tuple of (file_uploaded, file_path)
    """
    # Show supported formats
    show_supported_formats()
    
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
