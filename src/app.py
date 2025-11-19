import os
import time

from flask import Flask
from sqlalchemy.exc import OperationalError

from models import db
from routes import register_routes

def configure_database(app: Flask) -> None:
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        db_user = os.environ.get("DB_USER", "chatuser")
        db_password = os.environ.get("DB_PASSWORD", "chatpass")
        db_host = os.environ.get("DB_HOST", "db")
        db_port = os.environ.get("DB_PORT", "3306")
        db_name = os.environ.get("DB_NAME", "chat")
        database_url = (f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        max_retries = 10
        delay_seconds = 3

        for attempt in range(1, max_retries + 1):
            try:
                db.create_all()
                print("Database is ready")
                break
            except OperationalError as exc:
                if attempt == max_retries:
                    print("Database not ready after reaching retry limit")
                    raise
                print('"Database not ready yet"')
                time.sleep(delay_seconds)

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static")
    configure_database(app)
    register_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)