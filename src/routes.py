from __future__ import annotations
from datetime import datetime
from flask import Response, request
from models import ChatMessage, db

def register_routes(app):
    # Roman: This endpoint is a GET request by default, returns the static HTML
    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    # Anton: This API doesn't do anything with the room; it serves the same static HTML
    @app.route("/<room>")
    def room(room: str):
        return app.send_static_file("index.html")

    # Anton: POST request API, route: '/api/chat/<room>', accepts a chat message
    @app.route("/api/chat/<room>", methods=["POST"])
    def post_message(room: str):
        username = (request.form.get("username") or "").strip()
        if not username:
            username = "Anonymous"

        msg = (request.form.get("msg") or "").strip()
        if not msg:
            return "", 400

        timestamp = datetime.now()

        message = ChatMessage(room=room, username=username, message=msg, created_at=timestamp)

        db.session.add(message)
        db.session.commit()

        return "", 200

    # Roman: This GET endpoint returns the chat log for the room
    @app.route("/api/chat/<room>", methods=["GET"])
    def get_chat(room: str):
        messages = (
            ChatMessage.query.filter_by(room=room)
            .order_by(ChatMessage.created_at.asc())
            .all()
        )
        lines = [m.format_line() for m in messages]
        return Response("\n".join(lines), mimetype="text/plain")