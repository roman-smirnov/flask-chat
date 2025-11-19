"""
App entry point
"""

from flask import Flask
from routes import register_routes


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static")
    register_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='127.0.0.1',port=5000, debug=True)
