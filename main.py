from website import create_app
from website.views import socketio

app = create_app()

if __name__ == "__main__":

    socketio.init_app(app)
    socketio.run(app , debug=True , host='0.0.0.0', port=8080)
    