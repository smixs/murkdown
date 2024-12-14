"""
Simple test script for markitdown
"""
from pathlib import Path
from markitdown import MarkItDown

def main():
    print("Testing MarkItDown library...")
    
    # Initialize converter
    converter = MarkItDown()
    print("Converter initialized successfully")
    
    # Test text conversion
    test_text = "# Test Header\nThis is a test content."
    print("\nConverting text:")
    print("-" * 40)
    print(test_text)
    print("-" * 40)
    
    result = converter.convert_text(test_text)
    print("\nResult:")
    print("-" * 40)
    print(result)
    print("-" * 40)

if __name__ == "__main__":
    main() 