"""
Sidebar component for Streamlit interface
"""
import streamlit as st
from typing import Dict, Any

def sidebar_component() -> Dict[str, Any]:
    """
    Display sidebar with settings
    
    Returns:
        Dictionary of settings
    """
    with st.sidebar:
        st.markdown("## Settings")
        
        # Conversion settings
        st.markdown("### Conversion Settings")
        
        settings = {
            # Preview settings
            "show_preview": st.checkbox(
                "Show preview",
                value=True,
                help="Show preview of converted text"
            ),
            
            # Output settings
            "download_format": st.selectbox(
                "Download format",
                options=["Markdown (.md)", "Text (.txt)"],
                index=0,
                help="Choose output file format"
            ),
            
            # Advanced settings
            "advanced_settings": st.expander("Advanced Settings"),
        }
        
        # Advanced settings
        with settings["advanced_settings"]:
            settings.update({
                "preserve_images": st.checkbox(
                    "Preserve images",
                    value=True,
                    help="Save images in a separate folder"
                ),
                
                "extract_metadata": st.checkbox(
                    "Extract metadata",
                    value=True,
                    help="Include file metadata in output"
                ),
                
                "max_preview_length": st.slider(
                    "Preview length (chars)",
                    min_value=100,
                    max_value=1000,
                    value=500,
                    step=100,
                    help="Maximum length of preview text"
                )
            })
        
        # About section
        st.markdown("---")
        st.markdown("### About")
        st.markdown(
            "MarkItDown Web converts various file formats to Markdown "
            "for easy text analysis and processing."
        )
        
        # Version info
        st.markdown("---")
        st.markdown("v0.1.0")
    
    return settings
