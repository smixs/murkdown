# MarkItDown Web

Web interface for Microsoft MarkItDown library, allowing conversion of various file formats to Markdown for indexing and text analysis.

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
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

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