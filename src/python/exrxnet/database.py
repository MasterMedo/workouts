from proto.bodybuildingcom.exercise_pb2 import Exercise
from proto.bodybuildingcom.muscle_pb2 import Muscle

from src.python.database import ProtoDatabase

from config.python.config import (
    EXRXNET_EXERCISE_CSV_PATH,
    EXRXNET_MUSCLE_CSV_PATH,
)


class ExerciseDatabase(ProtoDatabase):
    def __init__(self):
        super().__init__(Exercise, EXRXNET_EXERCISE_CSV_PATH)


class MuscleDatabase(ProtoDatabase):
    def __init__(self):
        super().__init__(Muscle, EXRXNET_MUSCLE_CSV_PATH)
