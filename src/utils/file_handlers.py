"""
File handling utilities for MarkItDown Web
"""
from pathlib import Path
from typing import Union, BinaryIO, Optional
import tempfile
import os
import shutil

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
        shutil.rmtree(temp_dir)
        temp_dir.mkdir(parents=True, exist_ok=True)

def get_file_size(file_path: Union[str, Path]) -> str:
    """
    Get human-readable file size
    
    Args:
        file_path: Path to the file
        
    Returns:
        Human-readable size string
    """
    size_bytes = Path(file_path).stat().st_size
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def ensure_directories(*dirs: Union[str, Path]) -> None:
    """
    Ensure directories exist
    
    Args:
        *dirs: Directories to create
    """
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)