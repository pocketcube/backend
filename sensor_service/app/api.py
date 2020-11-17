import json
from app import socketio, mqtt, app
from datetime import datetime

from flask import send_file, request
from app import db

@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])

@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()


@app.route('/download')
def download():
    csv = db.get_csv()
    return send_file(csv, attachment_filename='pocketqube_data.csv', as_attachment=True)


@app.route('/details')
def detail():
    dataname = request.args.get('dataname')
    timestampStart = request.args.get('start')
    timestampEnd = request.args.get('end')
    if(timestampStart):
        timestampStart = datetime.fromtimestamp(int(timestampStart) / 1e3)
    if(timestampEnd):
        timestampEnd = datetime.fromtimestamp(int(timestampEnd) / 1e3)
    return db.get_json(dataname, timestampStart, timestampEnd)