py_binary(
  name = "analyse_workouts",
  srcs = ["analyse_workouts.py"],
  deps = [
    "//config/python:config"
  ],
  data = [
    "//datasets/workouts:workouts_txt",
    "//datasets/aliases:aliases_txt",
    "//datasets/exercises/bodybuilding.com:exercises_csv",
    "//datasets/exercises/enrichment:enrichment_csv",
  ],
)

py_binary(
  name = "analyse_muscle_strain",
  srcs = ["analyse_muscle_strain.py"],
  deps = [
    "//config/python:config"
  ],
  data = [
    "//datasets/workouts:workouts_txt",
    "//datasets/exercises/bodybuilding.com:exercises_csv",
  ],
)

py_library(
  name = "database",
  srcs = ["database.py"],
)
