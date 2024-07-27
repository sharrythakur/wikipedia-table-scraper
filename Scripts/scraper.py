import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from Utils.utils import save_table_to_csv


def scrape_wikipedia_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tables = soup.find_all("table", {"class": "wikitable"})
    if not tables:
        print("No tables found on the specified Wikipedia page.")
        return

    for i, table in enumerate(tables):
        df = pd.read_html(str(table))[0]
        save_table_to_csv(df, f"table_{i+1}.csv")
        print(f"Table {i+1} saved as table_{i+1}.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scraper.py <Wikipedia URL>")
        sys.exit(1)

    url = sys.argv[1]
    scrape_wikipedia_tables(url)
