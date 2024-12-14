# MarkItDown Web Interface

Web interface for converting various document formats to Markdown using the MarkItDown library.

## Features

- Convert various document formats to Markdown
- Supported formats: PDF, DOCX, TXT, and more
- Simple drag-and-drop interface
- Real-time conversion preview

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd markitdown
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app locally:

```bash
# Запуск через основной файл
streamlit run src/app.py

# Или напрямую через страницу
streamlit run src/pages/home.py
```

## Project Structure
```
markitdown/
├── src/
│   ├── app.py          # Entry point
│   ├── pages/
│   │   ├── home.py     # Main page
│   │   └── settings.py # Settings page
│   ├── components/     # UI components
│   └── utils/         # Utility functions
├── requirements.txt
└── README.md
```

## Environment Variables

Create a `.env` file with the following variables:

```
# Add any required API keys or configuration here
```

## Live Demo

Visit [Streamlit Cloud](https://streamlit.io) to see the live demo.

## License

MIT 