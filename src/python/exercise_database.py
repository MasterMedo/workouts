from proto.exercise_pb2 import Exercise

from src.python.database import ProtoDatabase
from src.python.bodybuildingcom.database import ExerciseDatabase as BBDB
from src.python.exrxnet.database import ExerciseDatabase as ENDB

from config.python.preferred_exercise_aliases import PREFERRED_EXERCISE_ALIASES


def unify_exercise_protos(bodybuildingcom_exercise, exrxnet_exercise):
    return Exercise(
        name="",
        preferred_alias="",
        muscle_weight_percentage={},
        percentage_of_bodyweight_lifted=0.23,
        percentage_of_bodyweight_lifted_source_url="",
    )


class ExerciseDatabase(ProtoDatabase):
    def __init__(self):
        super().__init__(Exercise)
        bodybuildingcom_database = BBDB()
        exrxnet_database = ENDB()

        for preferred_alias in PREFERRED_EXERCISE_ALIASES:
            self.messages[preferred_alias] = unify_exercise_protos(
                bodybuildingcom_database.get_from_alias(preferred_alias),
                exrxnet_database.get_from_alias(preferred_alias),
            )
