"""
Test all necessary imports
"""
import sys
print("Python path:", sys.path)

print("\nTesting imports...")
try:
    import markitdown
    print("✓ markitdown")
except ImportError as e:
    print("✗ markitdown:", e)

try:
    from markitdown import MarkItDown
    print("✓ MarkItDown class")
except ImportError as e:
    print("✗ MarkItDown class:", e)

try:
    import streamlit
    print("✓ streamlit")
except ImportError as e:
    print("✗ streamlit:", e)

try:
    from PIL import Image
    print("✓ Pillow")
except ImportError as e:
    print("✗ Pillow:", e)

try:
    import pytesseract
    print("✓ pytesseract")
except ImportError as e:
    print("✗ pytesseract:", e)

try:
    import speech_recognition
    print("✓ speech_recognition")
except ImportError as e:
    print("✗ speech_recognition:", e) 