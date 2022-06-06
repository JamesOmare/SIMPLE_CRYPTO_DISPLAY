from flask import Flask
from .config.config import Config
from .crypto_api.views import crypto

# app = Flask(__name__)

# from crypto_api import views
# from crypto_api import crypto_api

def create_app(config = Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    app.register_blueprint(crypto)

    return app