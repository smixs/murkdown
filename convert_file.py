#!/usr/bin/env python3
"""
Simple script to convert any file to markdown using markitdown library
Usage: python convert_file.py <input_file> [--full]
"""
import sys
import argparse
from pathlib import Path
from markitdown import MarkItDown

def convert_file(input_path: str, show_full: bool = False) -> None:
    """Convert file to markdown and save result"""
    input_file = Path(input_path)
    
    if not input_file.exists():
        print(f"Error: File '{input_file}' does not exist!")
        sys.exit(1)
    
    print(f"Converting file: {input_file}")
    print("-" * 60)
    
    # Initialize converter
    converter = MarkItDown()
    
    try:
        # Convert file
        result = converter.convert_local(str(input_file))
        
        # Create output filename
        output_file = input_file.with_suffix('.md')
        
        # Save result
        output_file.write_text(result.text_content)
        
        print(f"\nConversion successful!")
        print(f"Input file: {input_file}")
        print(f"Output file: {output_file}")
        print("\nPreview of the result:")
        print("-" * 60)
        
        # Show preview or full text
        if show_full:
            print(result.text_content)
        else:
            preview = result.text_content[:500] + "..." if len(result.text_content) > 500 else result.text_content
            print(preview)
            print("\nNote: This is just a preview. Use --full flag to see entire content")
            print(f"Or check the output file: {output_file}")
        
        print("-" * 60)
        
    except Exception as e:
        print(f"Error converting file: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert file to markdown')
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('--full', action='store_true', help='Show full converted text')
    
    args = parser.parse_args()
    convert_file(args.input_file, args.full)

if __name__ == "__main__":
    main() 