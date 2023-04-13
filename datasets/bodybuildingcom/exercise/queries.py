import csv
import random


exercises_filename = "exercises.csv"
target_muscle = "triceps"
surprise_me = False


def get_list_of_exercies(muscle, surprise):
    exercises = [d for d in data if d["muscle"].lower() == muscle.lower()]

    if len(exercises) == 0:
        return []

    if surprise:
        return [exercises[random.randrange(len(exercises))]["name"]]

    exercises = sorted(exercises, key=lambda e: -float(e["rating"]))
    return [e["name"] for e in exercises]


with open(exercises_filename) as f:
    data = list(csv.DictReader(f))

print(get_list_of_exercies(target_muscle, surprise_me))
