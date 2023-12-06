from apiflask import APIFlask

from config import config
from app.api import api_bp

app = APIFlask(__name__, title=config.PROJEDCT_NAME, version=config.VERSION, docs_ui='redoc')
app.description = config.DESCRIPTION
app.json.sort_keys = False

# Add blueprints
app.register_blueprint(api_bp.bp)

app.app_context().push()
