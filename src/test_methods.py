"""
Inspect markitdown methods
"""
from markitdown import MarkItDown

def main():
    print("Inspecting MarkItDown methods...")
    
    # Initialize converter
    converter = MarkItDown()
    
    # Get all methods
    methods = [method for method in dir(converter) if not method.startswith('_')]
    
    print("\nAvailable methods:")
    print("-" * 40)
    for method in methods:
        print(f"- {method}")
    print("-" * 40)

if __name__ == "__main__":
    main() 