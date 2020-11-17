import json
from io import StringIO
import pandas as pd
import sqlite3
from app import database, db_path
from datetime import datetime

class SensorData(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    timestamp = database.Column(database.DateTime, unique=False, nullable=False)
    sensor_name = database.Column(database.String(120), unique=False, nullable=False)
    sensor_value = database.Column(database.JSON, nullable=False)

database.create_all()


def get_csv():
    con = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * from sensor_data", con)
    s_buf = StringIO()
    df.to_csv(s_buf, index=False)
    con.close()
    s_buf.seek(0)
    return s_buf

def get_json(dataname, timestampStart, timestampEnd):
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

def save_data(topic,payload):
    sensor_data = SensorData(sensor_name=topic, timestamp=datetime.now(), sensor_value=payload )
    database.session.add(sensor_data)
    database.session.commit()