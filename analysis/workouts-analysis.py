import csv
import os

from datetime import datetime

FILE_DIR = os.path.dirname(__file__)
EXERCISES_PATH = os.path.join(
    FILE_DIR, "../datasets/exercises/bodybuilding.com/exercises.csv"
)
WORKOUTS_PATH = os.path.join(FILE_DIR, "../datasets/workouts/workouts.txt")
ALIASES_PATH = os.path.join(FILE_DIR, "../datasets/aliases/aliases.txt")


def parse_exercise_name(exercise_name):
    return exercise_name.lower().replace("-", " ")


with open(EXERCISES_PATH) as f:
    exercises = {
        parse_exercise_name(exercise["name"]) for exercise in csv.DictReader(f)
    }

with open(ALIASES_PATH) as f:
    aliases = {alias["alias"]: alias["exercise"] for alias in csv.DictReader(f)}

with open(WORKOUTS_PATH, "r") as f:
    workouts = f.read().split("\n\n")

data = []
for workout in workouts:
    workout = iter(workout.split("\n"))
    date, *description, time = next(workout).split()
    description = " ".join(description)
    date = datetime.strptime(date, "%d.%m.%Y.")

    for entry in workout:
        i = 0

        exercise_name = ""
        while i < len(entry) and (entry[i].isalpha() or entry[i].isspace()):
            exercise_name += entry[i]
            i += 1

        exercise_name = exercise_name.strip()
        if exercise_name not in exercises:
            if exercise_name in aliases:
                exercise_name = aliases[exercise_name]

        lifts = []
        while i < len(entry):
            weight = ""
            while i < len(entry) and entry[i] != "x":
                weight += entry[i]
                i += 1

            repetition = ""
            index = weight.rfind(" ")
            repetition = weight[index:] if index > -1 else weight
            weight = weight[:index] if index >= -1 else ""

            while i < len(entry) and entry[i] != " ":
                repetition += entry[i]
                i += 1

            try:
                sets, reps = map(int, repetition.split("x"))
                for w in weight.strip().split():
                    lifts.append((sets, reps, float(w)))
                else:
                    lifts.append((sets, reps, 0))
            except Exception:
                # print(date, exercise_name, e)
                pass

        for sets, reps, weight in lifts:
            data.append((date, exercise_name, sets, reps, weight))
        # print(date, description, time)
        # print(lifts)
    # print()

# with open('workouts.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

rcParams.update({"figure.autolayout": True})
sns.set(font_scale=1.5)

df = pd.DataFrame(data, columns=["date", "exercise", "sets", "reps", "weight"])
for exercise in df.groupby("exercise"):
    volumes = []
    maxes = []
    dates = []
    for day in exercise[1].groupby("date"):
        volume = 0
        max_ = 0
        for row in day[1].iterrows():
            row = row[1]
            volume += row.sets * row.reps * row.weight
            max_ = max(max_, row.weight)

        maxes.append(max_)
        volumes.append(volume)
        dates.append(day[0])

    if exercise[0] not in exercises:
        print(f"exercise: '{exercise[0]}' not found")
        continue

    if len(dates) > 5:
        # print('common: ' + exercise[0].title())
        dates = list(matplotlib.dates.date2num(dates))
        fig, axs = plt.subplots(2)
        fig.suptitle(exercise[0].title())
        axs[0].plot_date(dates, volumes, "b-")
        axs[0].set(ylabel="volume [kg]")
        axs[1].plot_date(dates, maxes, "r-")
        axs[1].set(ylabel="max [kg]")
        fig.autofmt_xdate()
        plt.show()
    # else:
    #     print('rare: ' + exercise[0].title())
