from flask import current_app, request, Response
from datetime import datetime


def register_routes(app):
    chat_rooms = {} # Anton: In-memory storage for chat messages per room
    
    # Roman: This endpoint is a GET request by default, returns the static HTML
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    

    # Anton: The API is also a GET request by default, returns the static HTML for any room
    @app.route('/<room>')
    def room(room):
        return app.send_static_file('index.html')
    
    # Anton: POST request API, route: '/api/chat/<room>', Accepts a chat message  
    @app.route('/api/chat/<room>', methods=['POST'])
    def post_message(room):
        # Extract user input, add default values in case of not providing one.
        username = request.form.get('username')
        if username == '':
            username = 'Anonymous'
        msg = request.form.get('msg', '')

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        formatted_message = f"[{timestamp}] {username}: {msg}"

        # If room does not exist, initialize a new one
        if room not in chat_rooms:
            chat_rooms[room] = []
        
        # Add message to room
        chat_rooms[room].append(formatted_message)

        return '', 200

    # Roman: This GET endpoint returns the chat log for the room
    @app.route("/api/chat/<room>", methods=["GET"])
    def get_chat(room: str):
        return Response('\n'.join(chat_rooms.get(room, '')), mimetype="text/plain")
