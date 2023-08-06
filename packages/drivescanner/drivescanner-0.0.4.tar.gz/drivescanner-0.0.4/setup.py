from setuptools import setup, find_packages
from pathlib import Path

# read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="drivescanner",
    version="0.0.4",
    python_requires=">=3.9",
    description="Scan your filesystem to look for files that are a potential GDPR risk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Wouter van Gils, Wim Verboom, Sem Frankenberg, Rick Flamand, Jeanine Schoonemann, Kjeld Vissers, Philip Vermeij, Matthijs Otten",
    author_email="service@cmotions.nl",
    url="https://dev.azure.com/Cmotions/Packages/_git/DriveScanner",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "spacy",
        "phonenumbers",
        "langdetect",
        "bs4",
        "pypdf>=3.9.1",
        "tqdm",
        "python-pptx",
        "docx2txt",
        "openpyxl",
    ],
    extras_require={
        "dev": [
            "black",
            "jupyterlab",
            "pytest>=6.2.4",
            "python-dotenv",
            "ipykernel",
            "twine",
            "seaborn",
        ],
    },
    # files to be shipped with the installation
    # after installation, these can be found with the functions in resources.py
    package_data={
        "drivescanner": [
            "data/*.csv",
            "data/*.txt",
            "notebooks/*tutorial*.ipynb",
        ]
    },
)
