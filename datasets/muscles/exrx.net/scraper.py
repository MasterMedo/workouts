import os
import csv
import requests

from bs4 import BeautifulSoup


muscles_filename = "muscles.csv"
bodyparts_filename = "bodyparts_tmp.csv"
fieldnames_m = [
    "id",
    "name",
    "segment",
    "position",
]
fieldnames_bp = [
    "id",
    "name",
]

with open("data.txt") as f:
    html = f.read()

def scrape_muscles(writer_bp: csv.DictWriter):
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
            writer_bp.writerow(fields)


with open(bodyparts_filename, "w") as f:
    writer_bp = csv.DictWriter(f, fieldnames=fieldnames_bp, lineterminator="\n")
    writer_bp.writeheader()
    scrape_muscles(writer_bp)
