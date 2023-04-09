load("@rules_proto//proto:defs.bzl", "proto_library")

proto_library(
  name = "exercise_proto",
  srcs = ["exercise.proto"],
  deps = [
    "//proto/bodybuildingcom:equipment_proto",
    "//proto/bodybuildingcom:muscle_proto",
  ],
)

proto_library(
  name = "muscle_proto",
  srcs = ["muscle.proto"],
)

proto_library(
  name = "equipment_proto",
  srcs = ["equipment.proto"],
)
