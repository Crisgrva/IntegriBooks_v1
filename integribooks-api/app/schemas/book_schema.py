from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    read = fields.Bool(missing=False)
    cover = fields.Str(required=False)
