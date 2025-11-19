from flask import current_app, request, Response


def register_routes(app):
    
    # Roman: This API is a GET request by default, returns the static HTML
    @app.route('/')
    def index():
        return app.send_static_file('index.html')
    

    # Anton: The API is also a GET request by default, returns the static HTML for any room
    @app.route('/<room>')
    def room(room):
        return app.send_static_file('index.html')
