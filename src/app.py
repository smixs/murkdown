import streamlit as st
from pathlib import Path
import sys

# Добавляем путь к src в PYTHONPATH
src_path = Path(__file__).parent
sys.path.append(str(src_path.parent))

# Импортируем основную страницу
from src.pages.home import main

if __name__ == "__main__":
    main() 