"""
CSR SALAD - Cofactor Specificity Reversal Semi-Automated Library Design
Setup configuration file
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="csr-salad",
    version="10.1",
    author="Jackson Cahn",
    author_email="",
    description="Computational tool for designing mutagenesis libraries to reverse NAD(P) cofactor specificity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "biopython>=1.79",
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "jupyterlab>=3.0.0",
        "ipython>=7.0.0",
        "ipywidgets>=7.6.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.ipynb"],
    },
    keywords="protein engineering, cofactor specificity, mutagenesis, NAD, NADP, library design",
    project_urls={
        "Bug Reports": "",
        "Source": "",
    },
)
