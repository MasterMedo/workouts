load("@rules_proto//proto:defs.bzl", "proto_library")
load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

proto_library(
  name = "muscle_proto",
  srcs = ["muscle.proto"],
)

proto_library(
  name = "equipment_proto",
  srcs = ["equipment.proto"],
)

proto_library(
  name = "exercise_proto",
  srcs = ["exercise.proto"],
  deps = [
    "//proto/bodybuildingcom:equipment_proto",
    "//proto/bodybuildingcom:muscle_proto",
  ],
)

py_proto_library(
  name = "equipment_pb2_py",
  srcs = ["equipment.proto"],
  visibility = ["//visibility:public"],
)

py_proto_library(
  name = "exercise_pb2_py",
  srcs = ["exercise.proto"],
  deps = [
    "//proto/bodybuildingcom:equipment_pb2_py",
    "//proto/bodybuildingcom:muscle_pb2_py",
  ],
  visibility = ["//visibility:public"],
)

py_proto_library(
  name = "muscle_pb2_py",
  srcs = ["muscle.proto"],
  visibility = ["//visibility:public"],
)
