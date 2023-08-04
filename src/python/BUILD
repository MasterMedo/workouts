py_binary(
  name = "analyse_workouts",
  srcs = ["analyse_workouts.py"],
  deps = [
    "//config/python:config"
  ],
  data = [
    "//datasets/workouts:workouts_txt",
    "//datasets/exercises:aliases_txt",
    "//datasets/bodybuildingcom:exercises_csv",
    "//datasets/exercises:enrichment_csv",
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
    "//datasets/bodybuildingcom:exercises_csv",
  ],
)

py_library(
  name = "database",
  srcs = ["database.py"],
)
