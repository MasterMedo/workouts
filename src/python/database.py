import csv


class ProtoDatabaseError(RuntimeError):
    pass


class ProtoDatabase:
    def __init__(self, proto, from_csv=None):
        self.messages = {}

        if from_csv is None:
            return

        with open(from_csv, "r") as f:
            reader = csv.DictReader(f)
            csv_fields = sorted(reader.fieldnames)
            proto_fields = sorted(field.name for field in proto.DESCRIPTOR.fields)
            if csv_fields != proto_fields:
                raise RuntimeError(
                    "Fields in the csv and the protobuf message don't match:"
                    f"\n  csv_fields: {csv_fields}"
                    f"\n  proto_fields: {proto_fields}"
                )

            for row in reader:
                message = proto()
                csv_row_to_proto_message(message, row)

    def get(self, message_id):
        return self.messages[message_id]


def csv_row_to_proto_message(row, message):
    for field_descriptor in message.DESCRIPTOR.fields:
        value = row[field_descriptor.name]
        match field_descriptor.type:
            case field_descriptor.TYPE_ENUM:
                if value in ["", "unspecified"]:
                    value = 0
                else:
                    prefix = field_descriptor.name.upper()
                    suffix = "_".join(value.upper().replace("-", "_").split())
                    name = prefix + "_" + suffix
                    value = field_descriptor.enum_type.values_by_name[name].number
            case field_descriptor.TYPE_STRING:
                pass
            case field_descriptor.TYPE_FLOAT:
                value = float(value)
            case default:
                raise RuntimeError(
                    f"The type of the field: {default} is not supported."
                )
        if value is not None:
            try:
                setattr(message, field_descriptor.name, value)
            except AttributeError as e:
                raise RuntimeError(
                    f"Field '{field_descriptor.name}' of the proto"
                    f"'{message.DESCRIPTOR.name}' can't be set to a value '{value}'.",
                    e,
                )
