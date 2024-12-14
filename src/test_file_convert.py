"""
Test file conversion with markitdown
"""
from pathlib import Path
from markitdown import MarkItDown

def main():
    print("Testing MarkItDown file conversion...")
    
    # Initialize converter
    converter = MarkItDown()
    print("Converter initialized successfully")
    
    # Test file conversion
    test_file = Path("test.txt").absolute()
    print(f"\nConverting file: {test_file}")
    print("-" * 40)
    
    with open(test_file, "r") as f:
        print("Original content:")
        print(f.read())
    
    print("-" * 40)
    result = converter.convert_local(str(test_file))
    
    print("\nConversion Result:")
    print("-" * 40)
    print(f"Title: {result.title or 'No title'}")
    print("\nContent:")
    print(result.text_content)
    print("-" * 40)
    
    # Save the result
    output_file = Path("output.md")
    output_file.write_text(result.text_content)
    print(f"\nResult saved to: {output_file.absolute()}")

if __name__ == "__main__":
    main() 