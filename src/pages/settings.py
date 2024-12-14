"""
MarkItDown Web - Settings page
"""
import streamlit as st
from pathlib import Path
from src.utils.converters import MarkdownConverter

# Configure page
st.set_page_config(
    page_title="Settings - MarkItDown Web",
    page_icon="⚙️",
    layout="wide"
)

def main():
    """Settings page main function"""
    st.title("Settings")
    
    # Initialize converter for format info
    converter = MarkdownConverter()
    
    # Display supported formats
    st.markdown("## Supported File Formats")
    formats = converter.get_supported_formats()
    
    # Group formats by type
    format_groups = {
        "Documents": ["pdf", "docx", "pptx", "xlsx"],
        "Images": ["png", "jpg", "jpeg"],
        "Audio": ["mp3", "wav"],
        "Text": ["txt", "html"]
    }
    
    # Create columns for each group
    cols = st.columns(len(format_groups))
    
    # Display formats by group
    for col, (group, group_formats) in zip(cols, format_groups.items()):
        with col:
            st.markdown(f"### {group}")
            for fmt in group_formats:
                mime_type = formats.get(fmt, "Unknown")
                st.markdown(f"- .{fmt} ({mime_type})")
    
    # System information
    st.markdown("## System Information")
    
    # Display paths
    st.markdown("### Paths")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Temporary Files**")
        if 'temp_dir' in st.session_state:
            st.code(str(st.session_state.temp_dir))
        else:
            st.markdown("*Not initialized*")
    
    with col2:
        st.markdown("**Output Directory**")
        st.code(str(Path.cwd() / "data" / "outputs"))
    
    # Version information
    st.markdown("## Version Information")
    st.markdown("- **MarkItDown Web:** v0.1.0")
    st.markdown("- **markitdown library:** 0.0.1a2")
    st.markdown("- **Streamlit:** " + st.__version__)

if __name__ == "__main__":
    main()
