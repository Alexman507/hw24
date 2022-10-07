from marshmallow import fields, Schema, validates_schema

VALID_CMD_PARAMS: Iterable[str] = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex',
)


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd1'] not in VALID_CMD_PARAMS:
            raise ValidationError('Invalid "cmd"')

        return values


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
