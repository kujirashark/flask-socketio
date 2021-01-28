#!/usr/bin/python
# -*- coding: UTF-8 -*
"""
******************************************************************************
*  Copyright (C) 2020~2021 lzl
*  版权所有。
******************************************************************************
@file_name: application.py
@author：lzl
@create date:  下午8:50
@description：
@update date： 
@file url:
@git path：
"""

from flask import Flask, render_template, request
from flask_gzip import Gzip
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./templates', static_folder="",
            static_url_path="", )

app.config['SECRET_KEY'] = 'secret!'
gzip = Gzip(app)
socketio = SocketIO(app)

count = 0


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my_event', namespace='/test')
def test_message(message):
    global count
    count += 1
    emit('my_response', {"count": count, 'data': message['data']})


@socketio.on('my_broadcast_event', namespace='/test')
def test_messagebroad(message):
    global count
    count += 1
    emit('my_response', {"count": count,
                         'data': message['data']}, broadcast=True)


@socketio.on('connect', namespace='/test')
def test_connect():
    print('connected')
    global count
    count += 1
    emit('my_response', {"count": count, 'data': 'Connected'})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


if __name__ == '__main__':
    socketio.run(app, port=8888, host='0.0.0.0', debug=True)
