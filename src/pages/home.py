"""
MarkItDown Web - Main application file
"""
import streamlit as st
from pathlib import Path
import tempfile
import os

# Configure the page
st.set_page_config(
    page_title="MarkItDown Web",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    st.title("MarkItDown Web")
    st.subheader("Convert documents to Markdown format")

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf", "docx", "pptx", "xlsx", "png", "jpg", "jpeg", "mp3", "wav", "html", "txt"],
        help="Select a file to convert to Markdown",
    )

    if uploaded_file is not None:
        # File info
        st.write("File details:")
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / 1024:.2f} KB",
            "File type": uploaded_file.type,
        }
        st.json(file_details)

        # Process button
        if st.button("Convert to Markdown"):
            with st.spinner("Converting..."):
                # TODO: Implement conversion logic
                st.success("Conversion completed!")
                st.markdown("### Preview:")
                st.text("Preview will be shown here")

if __name__ == "__main__":
    main() 