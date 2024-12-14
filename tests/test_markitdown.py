"""
Test markitdown library functionality
"""
import pytest
from pathlib import Path
from markitdown import MarkItDown

def test_markitdown_initialization():
    """Test that we can initialize MarkItDown"""
    converter = MarkItDown()
    assert converter is not None

def test_text_conversion():
    """Test basic text conversion"""
    converter = MarkItDown()
    test_text = "Hello, World!"
    result = converter.convert_text(test_text)
    assert isinstance(result, str)
    assert "Hello, World!" in result

def test_file_conversion(tmp_path):
    """Test file conversion with a simple text file"""
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_content = "# Test Header\nThis is a test content."
    test_file.write_text(test_content)
    
    converter = MarkItDown()
    result = converter.convert_file(test_file)
    
    assert isinstance(result, str)
    assert "Test Header" in result
    assert "test content" in result.lower() 