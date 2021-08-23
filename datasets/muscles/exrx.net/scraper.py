import csv

from bs4 import BeautifulSoup


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
            body_part = li.find("a").text.strip()
            fields = {
                "id": body_part.lower().replace(" ", "-"),
                "name": body_part,
            }
            writer_bp.writerow(fields)


with open("bodyparts.csv", "w") as f:
    writer_bp = csv.DictWriter(f, fieldnames=fieldnames_bp, lineterminator="\n")
    writer_bp.writeheader()
    scrape_muscles(writer_bp)
