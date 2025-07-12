from flask import Flask
from app.routes import user_routes, item_routes, admin_routes
from .config import Config


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_routes.user_bp)
    app.register_blueprint(item_routes.item_bp)
    app.register_blueprint(admin_routes.admin_bp)

    return app