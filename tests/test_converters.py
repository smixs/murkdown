"""
Tests for the converters module
"""
import pytest
from pathlib import Path
from src.utils.converters import detect_file_type, convert_to_markdown, extract_metadata, ConversionError

def test_detect_file_type():
    """Test file type detection"""
    test_files = {
        "test.pdf": "application/pdf",
        "test.docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "test.txt": "text/plain",
        "test.unknown": "application/octet-stream",
    }
    
    for filename, expected_type in test_files.items():
        assert detect_file_type(Path(filename)) == expected_type

def test_convert_to_markdown():
    """Test markdown conversion"""
    test_file = Path("test.txt")
    result = convert_to_markdown(test_file)
    assert isinstance(result, str)
    assert "test.txt" in result
    assert "Content will be converted here" in result

def test_extract_metadata():
    """Test metadata extraction"""
    test_file = Path(__file__)  # Use this test file itself
    metadata = extract_metadata(test_file)
    
    assert isinstance(metadata, dict)
    assert "filename" in metadata
    assert "size" in metadata
    assert "type" in metadata
    assert metadata["filename"] == test_file.name
    assert metadata["type"] == "text/x-python" 