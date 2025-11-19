from flask import current_app, request, Response


def register_routes(app):
    
    # Roman: This endpoint is a GET request by default, returns the static HTML
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    

    # Anton: The API is also a GET request by default, returns the static HTML for any room
    @app.route('/<room>')
    def room(room):
        return app.send_static_file('index.html')

    # Roman: This GET endpoint returns the chat log for the room
    @app.route("/api/chat/<room>", methods=["GET"])
    def get_chat(room: str):
        demo_chat = (
            "[2024-09-10 14:00:51] Roman Smirnov: Hello World! \n"
            + f"[2024-09-10 14:01:12] Anton Nahhas: Hello room {room}!.\n"
            + f"[2024-09-10 14:02:51] Roman Smirnov: Hello room {room}!\n"
            + f"[2024-09-10 14:03:51] Anton Nahhas: Hello room {room}!\n"
        )
        return Response(demo_chat, mimetype="text/plain")