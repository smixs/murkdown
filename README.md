# MarkItDown Web

Web interface for Microsoft MarkItDown library, allowing conversion of various file formats to Markdown for indexing and text analysis.

## Project Status

### Library Testing Results

We have tested the `markitdown` library (version 0.0.1a2) and discovered the following:

1. **Available Methods**:
   - `convert` - General conversion method
   - `convert_local` - Convert local files
   - `convert_response` - Convert HTTP responses
   - `convert_stream` - Convert data streams
   - `convert_url` - Convert content from URLs
   - `register_page_converter` - Register custom page converters

2. **File Conversion**:
   - Method to use: `convert_local(file_path)`
   - Returns: `DocumentConverterResult` object with attributes:
     - `text_content` - Converted markdown text
     - `title` - Document title (if available)

3. **Supported Features**:
   - Markdown formatting preservation
   - Headers
   - Lists
   - Bold and italic text
   - Code blocks
   - Blockquotes
   - Horizontal rules
   - Links

4. **Dependencies**:
   ```
   # Main Library
   markitdown>=0.0.1a2

   # Document Processing
   python-docx>=0.8.11  # For Word documents
   PyPDF2>=3.0.0  # For PDF files
   openpyxl>=3.1.2  # For Excel files
   python-pptx>=0.6.21  # For PowerPoint files

   # Image Processing
   Pillow>=10.0.0  # Base image processing
   pytesseract>=0.3.10  # OCR engine
   exifread>=3.0.0  # EXIF metadata

   # Audio Processing
   SpeechRecognition>=3.10.0  # Speech to text
   pydub>=0.25.1  # Audio file handling

   # HTML Processing
   beautifulsoup4>=4.12.0  # HTML parsing
   wikipedia-api>=0.6.0  # Wikipedia processing
   html2text>=2020.1.16  # HTML to markdown
   ```

5. **Usage Example**:
   ```python
   from markitdown import MarkItDown
   from pathlib import Path

   # Initialize converter
   converter = MarkItDown()

   # Convert local file
   file_path = Path("document.txt")
   result = converter.convert_local(str(file_path))

   # Access conversion result
   markdown_text = result.text_content
   document_title = result.title

   # Save result
   output_file = Path("output.md")
   output_file.write_text(result.text_content)
   ```

## Features

- Convert various file formats to Markdown
- Extract text and metadata
- OCR for images
- Audio transcription
- Structured output
- File preview and download
- Basic text analytics

## Supported Formats

- PDF (.pdf)
- PowerPoint (.pptx)
- Word (.docx)
- Excel (.xlsx)
- Images (with EXIF metadata and OCR)
- Audio (EXIF metadata and speech transcription)
- HTML (special Wikipedia processing)
- Text formats (csv, json, xml)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/markitdown-web.git
cd markitdown-web
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install system dependencies:
   - **Tesseract OCR**:
     - macOS: `brew install tesseract`
     - Ubuntu/Debian: `sudo apt-get install tesseract-ocr`
     - Windows: Download installer from official GitHub repository

## Usage

Run the application:
```bash
streamlit run src/pages/home.py
```

## Development

1. Install development dependencies:
```bash
pip install pytest black flake8
```

2. Run tests:
```bash
pytest tests/
```

3. Format code:
```bash
black .
flake8
```

## Project Structure

```
markitdown-app/
├── README.md                # Documentation
├── requirements.txt         # Dependencies
├── .gitignore              # Git ignore rules
├── .streamlit/             # Streamlit configuration
├── src/                    # Source code
│   ├── utils/             # Utility functions
│   ├── components/        # Streamlit components
│   └── pages/            # Application pages
├── tests/                # Tests
└── data/                # Data directory
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 