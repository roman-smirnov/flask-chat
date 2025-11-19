"""
App entry point
"""

from flask import Flask
from routes import register_routes


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", static_url_path="")
    register_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)  # Debug 
