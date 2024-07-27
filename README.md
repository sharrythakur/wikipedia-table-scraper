# Wikipedia Table Scraper

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

## Overview

The Wikipedia Table Scraper is a simple yet powerful tool designed to extract tables from Wikipedia pages and save them as CSV files. This tool is perfect for anyone looking to perform data extraction and analysis on structured data from Wikipedia.

## Features

- **Easy to Use**: Simple command-line interface.
- **Fast**: Efficient scraping with minimal dependencies.
- **Flexible**: Handles multiple tables on a single page.
- **Portable**: Outputs tables in CSV format for easy analysis.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/wikipedia-table-scraper.git
    cd wikipedia-table-scraper
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To scrape tables from a specific Wikipedia page, run the following command:
```sh
python scraper.py "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
