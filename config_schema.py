from marshmallow import Schema, fields, validate, EXCLUDE


class AppSchema(Schema):
    app_mode = fields.Str(required=True, validate=validate.OneOf(['development', 'testing', 'stage', 'production']))
    app_port = fields.Int(required=True)


class DatabaseSchema(Schema):
    db_host = fields.Str(required=True)
    db_port = fields.Int(required=True)
    db_user = fields.Str(required=True)
    db_password = fields.Str(required=True)
    db_name = fields.Str(required=True)


class DatabaseSchemas(Schema):
    mariadb = fields.Nested(DatabaseSchema)


class LineBotSchema(Schema):
    access_token = fields.Str(required=True)
    user_id = fields.Str(required=True)


class ConfigsSchema(Schema):
    app = fields.Nested(AppSchema)
    database = fields.Nested(DatabaseSchemas)
    line_bot = fields.Nested(LineBotSchema)


class PyprojectSchema(Schema):
    name = fields.Str(load_default='Project Name')
    version = fields.Str(load_default='0.0.0')
    description = fields.Str(load_default='Project Description')

    class Meta:
        unknown = EXCLUDE  # exclude unknown fields
