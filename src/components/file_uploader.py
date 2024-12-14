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
    # File uploader with custom styling
    uploaded_file = st.file_uploader(
        "Drop your file here",
        type=list(SUPPORTED_FORMATS.keys()),
        help="Select a file to convert to Markdown format",
        key="file_uploader",
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        # Show file info with custom styling
        st.markdown(
            f"""
            <div class="info-card">
                <h4 style='margin: 0; color: #ffffff;'>Selected File</h4>
                <div style='margin: 0.5rem 0;'>
                    <p style='margin: 0.2rem 0;'>
                        <strong>Name:</strong> {uploaded_file.name}
                    </p>
                    <p style='margin: 0.2rem 0;'>
                        <strong>Size:</strong> {len(uploaded_file.getvalue()) / 1024:.1f} KB
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Save file
        temp_file = save_uploaded_file(uploaded_file, temp_dir)
        if temp_file:
            return True, temp_file
        else:
            st.error("❌ Failed to save uploaded file")
    
    return False, None
