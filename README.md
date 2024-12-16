# MurkDown 🐱

Purrfect for LLMs - converts any document into LLM-optimized Markdown format.

![MurkDown](static/images/cat.png)

## Features

- Convert various document formats to Markdown  
- Supported formats: PDF, DOCX, TXT, Excel, HTML, and more  
- Simple drag-and-drop interface  
- Real-time conversion preview  
- LLM-optimized output format  

## Installation

1. Clone the repository:
```bash
git clone https://github.com/smixs/murkdown.git
cd murkdown
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

## Project Structure
```
murkdown/
├── app.py             # Entry point
├── src/
│   ├── pages/
│   │   ├── home.py     # Main page
│   │   └── settings.py # Settings page
│   ├── components/     # UI components
│   └── utils/         # Utility functions
├── requirements.txt
└── README.md
```

## Live Demo

Visit [Streamlit Cloud](https://murkdown.streamlit.app/) to see the live demo.

## License

MIT
