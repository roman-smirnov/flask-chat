from flask import current_app, request, Response


def register_routes(app):

    @app.route("/", defaults={"room": "general"})
    @app.route("/<room>")
    def room_page(room: str):
        """ Returns index.html for any room """
        return current_app.send_static_file("index.html")
