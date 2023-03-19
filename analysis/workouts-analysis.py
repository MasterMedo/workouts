import csv
import os
import re
import matplotlib.pyplot as plt

from collections import defaultdict
from datetime import datetime, timedelta
from matplotlib import rcParams

import pandas as pd
import matplotlib
import seaborn as sns

FILE_DIR = os.path.dirname(__file__)
EXERCISES_PATH = os.path.join(
    FILE_DIR, "../datasets/exercises/bodybuilding.com/exercises.csv"
)
EXERCISES_ENRICHMENT_PATH = os.path.join(
    FILE_DIR, "../datasets/exercises/enrichment/enrichment.csv"
)
WORKOUTS_PATH = os.path.join(FILE_DIR, "../datasets/workouts/workouts.txt")
ALIASES_PATH = os.path.join(FILE_DIR, "../datasets/aliases/aliases.txt")
MY_BODYWEIGHT = 70


def parse_exercise_name(exercise_name):
    return exercise_name.lower().replace("-", " ")


with open(EXERCISES_PATH) as f:
    exercises = {
        parse_exercise_name(exercise["name"]): exercise
        for exercise in csv.DictReader(f)
    }

aliases = {}
with open(ALIASES_PATH) as f:
    for alias in csv.DictReader(f):
        if alias["exercise"] not in exercises:
            raise RuntimeError(
                f"Faulty configuration of the aliases file: '{ALIASES_PATH}'. The exercise '{alias['exercise']}' doesn't map to any exercise in the exercises file: '{EXERCISES_PATH}'. The alias '{alias['alias']} needs to be reconfigured."
            )
        if alias["alias"] in aliases:
            raise RuntimeError(
                f"Faulty configuration of the aliases file: '{ALIASES_PATH}'. The alias '{alias['alias']} has already been configured to map to the exercise '{aliases[alias['alias']]}', so it can't be remapped to '{alias['exercise']}'. Please delete one of the entries."
            )
        aliases[alias["alias"]] = alias["exercise"]

enrichments = defaultdict(dict)
with open(EXERCISES_ENRICHMENT_PATH) as f:
    for exercise in csv.DictReader(f):
        if exercise["name"] not in exercises:
            raise RuntimeError(
                f"Faulty configuration of the exercises enrichment file: '{EXERCISES_ENRICHMENT_PATH}', the exercise '{exercise['name']}' doesn't exist in the exercises file: '{EXERCISES_PATH}'."
            )
        enrichments[exercise["name"]] = exercise

with open(WORKOUTS_PATH, "r") as f:
    workouts = f.read().split("\n\n")

workouts_sets_and_reps = []
for workout in workouts:
    workout = iter(workout.split("\n"))
    date, *description, time = next(workout).split()
    description = " ".join(description)
    date = datetime.strptime(date, "%d.%m.%Y.")

    for entry in workout:
        tokens = entry.strip().split()
        exercise_name_arr = []
        # TODO(mastermedo): refactor last_weight into an array because the following line might be written: 'lat pull down 50 30 40 1x12'. This should be evaluated as '50 1x12 30 1x12 40 1x12'.
        last_weight = 0
        still_entering_the_exercise_name = True
        durations = []
        sets_and_reps = []
        for i, token in enumerate(tokens):
            # word in the exercise name
            if token.isalpha():
                if not still_entering_the_exercise_name:
                    raise RuntimeError(
                        f"Exercise names can't contain words with non-alphabetic characters. Word '{token}' can't be the after the word '{tokens[i-1]}' in the exercise line: '{entry}'. If you meant to write a number, write it in the textual form e.g. '30' should be written as 'thirty'. A full example would be 'thirty degree incline bench 80 4x12'"
                    )
                exercise_name_arr.append(token)
            # weight in default units e.g. 80.5
            elif re.match(r"^-?\d*\.?\d+$", token):
                if i >= len(tokens) - 1:
                    raise RuntimeError(
                        f"Weight '{token}' can't be the last word in the exercise line: '{entry}'. Number of sets and reps or duration of the exercise needs to be added after the weight. E.g. 'wide grip lat pull down 20 4x12' (20kg for 4 sets of 12 reps) or 'tenis :1:30'"
                    )

                # ########## BEGIN DATA BACKFILL ##########
                # TODO(mastermedo): remove this code
                weight = float(token)
                exercise_name = " ".join(exercise_name_arr)
                if exercise_name in aliases:
                    exercise_name = aliases[exercise_name]
                if weight <= 0:
                    if "is bodyweight" not in exercises[exercise_name]:
                        enrichments[exercise_name]["is bodyweight"] = True
                # ########## END DATA BACKFILL ##########

                # TODO(mastermedo): if the weight is <= 0; check if the current exercise is a bodyweight exercise. If it is; add the bodyweight to the weight, if it's not; throw an error, if it's not defined yet; throw an error to add it to the data enriching
                last_weight = float(token)
            # TODO(mastermedo): what if an exercise has a duration and sets/reps immediately one after the other? That should be marked as a single exercise indicating how long it took to do those reps and sets. Currently it is being marked as a completely separate exercise.
            # duration e.g. ::5 or 1:34:45 or :189:
            elif match_object := re.match(r"^(\d*):(\d*):(\d*)$", token):
                hours, minutes, seconds = map(
                    lambda x: int(x) if x else 0, match_object.groups()
                )
                durations.append((seconds + 60 * minutes + 3600 * hours, last_weight))
            # sets and reps e.g. 5x10
            elif match_object := re.match(r"^(\d*)x(\d+)$", token):
                sets, reps = match_object.groups()
                if not sets:
                    sets = "0"
                sets_and_reps.append((int(sets), int(reps), last_weight))
            # custom unit e.g. 5km or 12lb
            elif match_object := re.match(r"^-?\d*\.?\d+\w+$", token):
                # TODO(mastermedo): implement custom units support
                continue
            else:
                raise RuntimeError(
                    f"Word '{token}' was not recognised as a valid word in the exercise line: '{entry}'. Valid words can be:\n  exercise names - alphabetic strings, e.g. thirty degree incline bench press,\n  weight - decimal numbers, e.g. 40.25\n  duration - hours:minutes:seconds, e.g. 5::20\n  sets and reps - number of sets and reps separated by the letter 'x', e.g. 5x10"
                )

        exercise_name = " ".join(exercise_name_arr)
        if exercise_name in aliases:
            exercise_name = aliases[exercise_name]

        for sets, reps, weight in sets_and_reps:
            workouts_sets_and_reps.append((date, exercise_name, sets, reps, weight))

        # TODO(mastermedo): implement tracking durations
        for duration, weight in durations:
            pass

# with open("workouts.csv", "w") as f:
#     writer = csv.writer(f)
#     writer.writerows(workouts_sets_and_reps)


rcParams.update({"figure.autolayout": True})
sns.set(font_scale=1.5)

df = pd.DataFrame(
    workouts_sets_and_reps, columns=["date", "exercise", "sets", "reps", "weight"]
)
for exercise in df.groupby("exercise"):
    volumes = []
    maxes = []
    dates = []
    for day in exercise[1].groupby("date"):
        volume = 0
        max_ = 0
        for row in day[1].iterrows():
            row = row[1]
            weight = row.weight
            if (
                "is bodyweight" in enrichments[exercise[0]]
                and enrichments[exercise[0]]["is bodyweight"]
            ):
                weight += MY_BODYWEIGHT
            volume += row.sets * row.reps * weight
            max_ = max(max_, weight)

        maxes.append(max_)
        volumes.append(volume)
        dates.append(day[0])

    if exercise[0] not in exercises:
        print(f"exercise: '{exercise[0]}' not found")
        continue

    if len(dates) > 5 and dates[-1] > datetime.now() - timedelta(weeks=12):
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
