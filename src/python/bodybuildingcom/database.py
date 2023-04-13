from proto.bodybuildingcom.exercise_pb2 import Exercise

from src.python.database import ProtoDatabase

from config.python.config import (
    BODYBUILDINGCOM_EXERCISE_CSV_PATH,
)


class ExerciseDatabase(ProtoDatabase):
    def __init__(self):
        super().__init__(Exercise, BODYBUILDINGCOM_EXERCISE_CSV_PATH)
