from apiflask import APIBlueprint
from flask import redirect

from app.schema import api_schema

bp = APIBlueprint('api', __name__, url_prefix=None)


@bp.get("/")
@bp.doc(description="API Documentation")
def index():
    return redirect("/docs")


@bp.get('/status')
@bp.doc(description="API Status")
@bp.output(api_schema.ResponseSchema)
def status():
    return {"status_code": 200, "message": "API is running"}
