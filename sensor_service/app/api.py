import json
from app import socketio, mqtt, app, db_path

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

from io import StringIO
import pandas as pd
import sqlite3
from flask import send_file

@app.route('/download')
def download():
    con = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * from sensor_data", con)
    s_buf = StringIO()
    df.to_csv(s_buf, index=False)
    con.close()
    s_buf.seek(0)
    return send_file(s_buf, attachment_filename='pocketqube_data.csv', as_attachment=True)
