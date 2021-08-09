import csv
import requests

from bs4 import BeautifulSoup


headers = {
    "authority": "www.bodybuilding.com",
    "x-requested-with": "XMLHttpRequest",
}

params = (("undefined", ""),)

with open("scraping.csv", "a") as f:
    writer = csv.DictWriter(
        f, fieldnames=["name", "muscle", "equipment"], lineterminator="\n"
    )

    for i in range(1, 878):  # 878 throws maximal tries exceeded
        response = requests.get(
            f"https://www.bodybuilding.com/exercises/finder/{i}/",
            headers=headers,
            params=params,
        )

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find("div", class_="ExCategory-results")

        for result in results.find_all("div", class_="ExResult-row"):
            fields = {
                "name": result.find("h3", class_="ExResult-resultsHeading"),
                "muscle": result.find("div", class_="ExResult-muscleTargeted"),
                "equipment": result.find("div", class_="ExResult-equipmentType"),
            }
            writer.writerow({k: v.find("a").text.strip() for k, v in fields.items()})
