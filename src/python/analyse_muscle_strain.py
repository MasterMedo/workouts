import csv

from datetime import datetime

from config.python.config import EXERCISES_PATH, WORKOUTS_PATH

with open(EXERCISES_PATH) as f:
    exercises = list(csv.DictReader(f))
names = {
    (exercise["name"].lower().replace("-", " "), exercise["muscle"])
    for exercise in exercises
}

with open(WORKOUTS_PATH) as f:
    workouts = f.read().split("\n\n")

data = []
for workout in workouts:
    workout = iter(workout.split("\n"))
    date, *description, time = next(workout).split()
    description = " ".join(description)
    date = datetime.strptime(date, "%d.%m.%Y.")

    for entry in workout:
        i = 0

        exercise = ""
        while i < len(entry) and (entry[i].isalpha() or entry[i].isspace()):
            exercise += entry[i]
            i += 1
        exercise = exercise.strip()

        muscles = [e[1] for e in names if e[0] == exercise.lower()]
        if len(muscles) != 1:
            continue
        muscle = muscles[0]

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
                # print(date, exercise, e)
                pass

        for sets, reps, weight in lifts:
            data.append((date, exercise, muscle, sets, reps, weight))
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

df = pd.DataFrame(
    data, columns=["date", "exercise", "muscle", "sets", "reps", "weight"]
)
for muscle in df.groupby("muscle"):
    volumes = []
    maxes = []
    dates = []
    for day in muscle[1].groupby("date"):
        volume = 0
        max_ = 0
        for row in day[1].iterrows():
            row = row[1]
            volume += row.sets * row.reps * row.weight
            max_ = max(max_, row.weight)

        maxes.append(max_)
        volumes.append(volume)
        dates.append(day[0])

    if len(dates) > 5:
        dates = list(matplotlib.dates.date2num(dates))
        fig, axs = plt.subplots(2)
        fig.suptitle(muscle[0].title())
        axs[0].plot_date(dates, volumes, "b-")
        axs[0].set(ylabel="volume [kg]")
        axs[1].plot_date(dates, maxes, "r-")
        axs[1].set(ylabel="max [kg]")
        fig.autofmt_xdate()
        plt.show()
