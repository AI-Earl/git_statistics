from marshmallow import Schema, fields


class ResponseSchema(Schema):
    status_code = fields.Integer(required=True, default=200, description="狀態碼")
    message = fields.String(required=True, default='', description="提示訊息")
