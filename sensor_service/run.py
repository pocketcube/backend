import eventlet
eventlet.monkey_patch()

from app import socketio, app

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)