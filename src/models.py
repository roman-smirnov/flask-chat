from __future__ import annotations
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()

class ChatMessage(db.Model):
    __tablename__ = "chat_messages"
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(255), nullable=False, index=True)
    username = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def format_line(self) -> str:
        timestamp = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {self.username}: {self.message}"