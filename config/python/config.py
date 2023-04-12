import os

BODYWEIGHT = 70

FILE_DIR = os.path.dirname(__file__)
EXERCISES_PATH = os.path.join(
    FILE_DIR, "../../datasets/exercises/bodybuilding.com/exercises.csv"
)
EXERCISES_ENRICHMENT_PATH = os.path.join(
    FILE_DIR, "../../datasets/exercises/enrichment/enrichment.csv"
)
WORKOUTS_PATH = os.path.join(FILE_DIR, "../../datasets/workouts/workouts.txt")
ALIASES_PATH = os.path.join(FILE_DIR, "../../datasets/aliases/aliases.txt")
