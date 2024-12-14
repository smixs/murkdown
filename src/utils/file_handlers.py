"""
File handling utilities for MarkItDown Web
"""
from pathlib import Path
from typing import Union, BinaryIO, Optional
import tempfile
import os

def save_uploaded_file(uploaded_file: BinaryIO, temp_dir: Union[str, Path]) -> Optional[Path]:
    """
    Save an uploaded file to a temporary directory
    
    Args:
        uploaded_file: The uploaded file object
        temp_dir: Directory to save the file in
        
    Returns:
        Path to the saved file or None if save failed
    """
    try:
        temp_dir = Path(temp_dir)
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        temp_path = temp_dir / uploaded_file.name
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return temp_path
    except Exception as e:
        print(f"Error saving file: {e}")
        return None

def cleanup_temp_files(temp_dir: Union[str, Path]) -> None:
    """
    Remove temporary files from directory
    
    Args:
        temp_dir: Directory to clean up
    """
    temp_dir = Path(temp_dir)
    if temp_dir.exists():
        for file in temp_dir.glob("*"):
            if file.is_file():
                try:
                    file.unlink()
                except Exception as e:
                    print(f"Error deleting {file}: {e}") 