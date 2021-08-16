import os
import csv
import requests

from bs4 import BeautifulSoup


exercises_filename = "exercises.csv"
fieldnames = ["id", "name", "muscle", "equipment", "description", "benefits", "instructions"]
headers = {
    "authority": "www.bodybuilding.com",
    "x-requested-with": "XMLHttpRequest",
}

params = (("undefined", ""),)


def scrape_exercises(writer: csv.DictWriter):
    """ """
    for i in range(1, 878):  # 878 throws maximal tries exceeded
        response = requests.get(
            f"https://www.bodybuilding.com/exercises/finder/{i}/",
            headers=headers,
            params=params,
        )

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find("div", class_="ExCategory-results")

        for result in results.find_all("div", class_="ExResult-row"):
            exercise_id = (
                result.find("h3", class_="ExResult-resultsHeading")
                .find("a")["href"]
                .removeprefix("/exercises/")
            )
            response = requests.get(
                f"https://www.bodybuilding.com/exercises/{exercise_id}/",
                headers=headers,
            )
            soup = BeautifulSoup(response.text, "html.parser")
            fields = {
                "id": exercise_id,
                "name": get_name(result),
                "muscle": get_muscle(result),
                "equipment": get_equipment(result),
                "description": get_description(soup),
                "benefits": get_benefits(soup),
                "instructions": get_instructions(soup),
                # "level": ,
                # "images": ,
            }
            writer.writerow(fields)


def get_name(soup: BeautifulSoup) -> str:
    result = soup.find("h3", class_="ExResult-resultsHeading")
    if result is None:
        return ""

    result = result.find("a")
    if result is None:
        return ""

    return result.text.strip()


def get_muscle(soup: BeautifulSoup) -> str:
    result = soup.find("div", class_="ExResult-muscleTargeted")
    if result is None:
        return ""

    result = result.find("a")
    if result is None:
        return ""

    return result.text.strip()


def get_equipment(soup: BeautifulSoup) -> str:
    result = soup.find("div", class_="ExResult-equipmentType")
    if result is None:
        return ""

    result = result.find("a")
    if result is None:
        return ""

    return result.text.strip()


def get_description(soup: BeautifulSoup) -> str:
    """Get description from the specific exercise page."""
    result = soup.find("div", class_="ExDetail-shortDescription")
    if result is None:
        return ""

    return result.text.strip()


def get_benefits(soup: BeautifulSoup) -> str:
    """Get benefits from the specific exercise page."""
    result = soup.find("div", class_="ExDetail-benefits")
    if result is None:
        return ""

    return "\n".join(
        li.text.strip() for li in result.find_all("li")
    )


def get_instructions(soup: BeautifulSoup) -> str:
    """Get benefits from the specific exercise page."""
    result = soup.find("div", itemprop="description")
    if result is None:
        return ""

    return "\n".join(
        li.text.strip() for li in result.find_all("li")
    )


if not os.path.isfile(exercises_filename):
    with open(exercises_filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        scrape_exercises(writer)
