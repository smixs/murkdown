from setuptools import setup, find_packages

setup(
    name="markitdown-web",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "markitdown>=0.0.1a2",
    ],
) 