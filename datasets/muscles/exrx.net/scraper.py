import os
import csv
import requests

from bs4 import BeautifulSoup


muscles_filename = "muscles.csv"
bodyparts_filename = "bodyparts.csv"
fieldnames_m = [
    "id",
    "name",
    "segment",
    "position",
]
fieldnamems_bp = [
    "id",
    "name",
]

headers = {
    "authority": "www.exrx.net",
    "x-requested-with": "XMLHttpRequest",
}

params = (("undefined", ""),)

bodyparts = []

with open("data.txt") as f:
    html = f.read()

def scrape_muscles(writer_bp: csv.DictWriter):
    """ """
    response = requests.get(
        f"https://www.exrx.net/Lists/Directory/",
        headers=headers,
        params=params,
    )

    soup = BeautifulSoup(html, "html.parser")
    columns = soup.find_all("div", class_="col-sm-6")

    for col in columns:
        col = col.find("ul")
        for li in col.find_all("li", recursive=False):
            bp = li.find("a").text.strip()
            fields = {
                "id": bp.lower().replace(" ", "-"),
                "name": bp,
            }
            writer.writerow(fields)

            prefix = ""
            for li2 in li.find_all("li"):
                a = li2.find("a", recursive=False)
                if a is None:
                    prefix = li2.text().split("<")[0]


with open(bodyparts_filename, "w") as f:
    writer_bp = csv.DictWriter(f, fieldnames=fieldnames_bp, lineterminator="\n")
    writer_bp.writeheader()
    scrape_muscles(writer_bp)
