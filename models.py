from marshmallow import fields, Schema, validates_schema


VALID_CMD_PARAMS =(
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex',
)


class RequestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd1'] not in VALID_CMD_PARAMS:
            raise ValidationError('Invalid "cmd"')

        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)