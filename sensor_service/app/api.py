import json
from app import socketio, mqtt, app, db_path, db
from datetime import datetime

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
from flask import send_file, request

@app.route('/download')
def download():
    con = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * from sensor_data", con)
    s_buf = StringIO()
    df.to_csv(s_buf, index=False)
    con.close()
    s_buf.seek(0)
    return send_file(s_buf, attachment_filename='pocketqube_data.csv', as_attachment=True)


@app.route('/details')
def detail():
    dataname = request.args.get('dataname')
    timestampStart = request.args.get('start')
    timestampEnd = request.args.get('end')
    if(timestampStart):
        timestampStart = datetime.fromtimestamp(int(timestampStart) / 1e3)
    if(timestampEnd):
        timestampEnd = datetime.fromtimestamp(int(timestampEnd) / 1e3)

    con = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * from sensor_data", con)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    if(timestampStart):
        df = df[df['timestamp'] >= timestampStart]
    if(timestampEnd):
        df = df[df['timestamp'] <= timestampEnd]
    if(dataname):
        df = df[df['sensor_value'].str.contains(dataname)]
    df['sensor_value'] = df['sensor_value'].apply(json.loads)
    df_json = df.to_json(orient="records")
    
    return df_json