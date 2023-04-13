import sqlite3

from proto.bodybuildingcom.exercise_pb2 import Exercise


PROTO_TYPE_TO_SQL_TYPE = {
    8: "BOOL",
    1: "DOUBLE",
    14: "VARCHAR(100)",
    2: "FLOAT",
    3: "INTEGER",
    5: "INTEGER",
    9: "VARCHAR(10000)",
}


def create_table_from_proto(database_connection, proto):
    table_name = proto.DESCRIPTOR.name
    table_fields = ", ".join(
        f"{field.name} {PROTO_TYPE_TO_SQL_TYPE[field.type]}"
        + (" PRIMARY KEY" if field.name == "id" else "")
        for field in proto.DESCRIPTOR.fields
    )
    database_connection.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {table_fields}
        )
        """
    )


if __name__ == "__main__":
    database_connection = sqlite3.connect("database/workouts.db")
    create_table_from_proto(database_connection, Exercise)
