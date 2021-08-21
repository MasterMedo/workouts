import os
import csv
import requests

from bs4 import BeautifulSoup


muscles_filename = "muscles.csv"
bodyparts_filename = "bodyparts.csv"
fieldnames_m = [
    "id",
    "name",
    "muscle",
    "equipment",
    "description",
    "benefits",
    "instructions",
]
fieldnamems_bp = []

headers = {
    "authority": "www.exrx.net",
    "x-requested-with": "XMLHttpRequest",
}

params = (("undefined", ""),)


def scrape_muscles(writer: csv.DictWriter):
    """ """
    response = requests.get(
        f"https://www.exrx.net/Lists/Directory/",
        headers=headers,
        params=params,
    )

    soup = BeautifulSoup(response.text, "html.parser")
    columns = soup.find_all("div", class_="col-sm-6")

    for col in columns:
        for ul in col.find_all("ul", recursive=False):
            for ul2 in ul.find_all("ul"):
                print(ul2)
                print()


scrape_muscles(None)
