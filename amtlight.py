from web import app
from web import socketio
import data


if __name__ == '__main__':
    data.start()
    socketio.run(app, host='0.0.0.0', port=80)
