import csv
import re
import requests
import traceback
from urllib.parse import urljoin, urldefrag

from bs4 import BeautifulSoup


exercises_filename = "exercises.csv"
fieldnames = [
    "id",
    "name",
    "force",
    # "utility",
    # "mechanics",
    "target",
    "synergist",
    "stabilizer",
    "dynamic stabilizer",
    "antagonist stabilizer",
    "instructions",
    # "equipment" ,
    # "level" ,
    # "images" ,
]
headers = {
    "x-requested-with": "XMLHttpRequest",
}


def get_name(soup: BeautifulSoup) -> str:
    tag = soup.find("h1", class_="page-title")
    return tag.text.strip()


def get_force(soup: BeautifulSoup) -> str:
    tag = soup.find("strong", string="Force:")
    if tag is None:
        return "unspecified"
    return tag.parent.find_next_sibling().a.text


def get_muscles(soup: BeautifulSoup) -> dict[str, str]:
    muscles = {}
    tag = soup.find(["h2", "h3"], string="Muscles")
    if tag is None:
        raise RuntimeError("No muscle information.")
    while True:
        tag = tag.find_next_sibling()
        if tag is None:
            break

        if tag.name != "p":
            continue

        group = tag.text.split("(")[0].lower()
        tag = tag.find_next_sibling()

        if tag is None or tag.name != "ul":
            break

        elements = ";".join(
            muscle for muscle in tag.find_all(string=True) if muscle != "None"
        )
        for group in group.split("/"):
            if group:
                group = re.sub(r"\s+", " ", group.strip())
                muscles[group.removesuffix("s")] = elements

    return muscles


def get_instructions(soup: BeautifulSoup) -> str:
    tag = soup.find("h2", string="Instructions")
    instructions = ""
    if tag is None:
        return instructions
    while True:
        tag = tag.find_next_sibling()
        if tag is None:
            break

        instructions += tag.text
        instructions += "\n\n"
    return instructions.removesuffix("\n")


if __name__ == "__main__":
    muscle_links = set()
    exercise_links = set()

    response = requests.get("https://exrx.net/Lists/Directory", headers)
    soup = BeautifulSoup(response.text, "html5lib")
    for content in soup.find_all("div", class_="col-sm-6"):
        for action_tag in content.find_all("a"):
            link = action_tag["href"].strip()
            if not link.startswith("http"):
                link = urljoin("https://exrx.net/Lists/", link)

            muscle_links.add(urldefrag(link)[0])

    for link in muscle_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html5lib")
        for list_item in soup.find_all("li"):
            action_tag = list_item.find("a", recursive=False)
            if action_tag is not None:
                link = action_tag["href"].strip()
                if not link.startswith("http"):
                    link = urljoin("https://exrx.net/Lists/", link)

                exercise_links.add(urldefrag(link)[0])

    f = open(exercises_filename, "a+")
    writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()

    for link in exercise_links:
        if link.startswith("https://exrx.net/WeightExercises/"):
            if any(
                tag in link for tag in ["Kettlebell", "OlympicLifts", "Other", "Power"]
            ):
                # These don't have any muscle information
                continue
            response = requests.get(link)
            soup = BeautifulSoup(response.text, "html5lib")
            try:
                fields = {
                    "id": link[33:],
                    "name": get_name(soup),
                    "force": get_force(soup),
                    "instructions": get_instructions(soup),
                    **get_muscles(soup),
                }

                writer.writerow(fields)
            except Exception:
                print(link)
                traceback.print_exc()
        elif link.startswith("https://exrx.net/Stretches/"):
            ...
        else:
            ...

    f.close()
