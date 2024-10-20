import os

from flask import Flask, jsonify
from whitenoise import WhiteNoise


def create_app(script_info=None):

    app = Flask(__name__, static_folder="staticfiles")

    WHITENOISE_MAX_AGE = 31536000 if not app.config["DEBUG"] else 0

    # configure WhiteNoise
    app.wsgi_app = WhiteNoise(
        app.wsgi_app,
        root=os.path.join(os.path.dirname(__file__), "staticfiles"),
        prefix="assets/",
        max_age=WHITENOISE_MAX_AGE,
    )

    @app.route("/")
    def hello_world():
        return jsonify(hello="world")

    return app
