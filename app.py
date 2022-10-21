#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
import time
from math import floor
import base64
import codecs

def decode(coded_string, have_it):
    try:
        if have_it: coded_string = coded_string+'=='
        coded_string = base64.b64decode(coded_string).decode('utf-8')
        coded_string = codecs.encode(coded_string, 'rot13')
        coded_string = coded_string[::-1]
        coded_string = base64.b64decode(coded_string).decode('utf-8')
        return coded_string
    except:
        return False

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():

    return render_template("index.html")

@app.route('/send-text', methods=['POST'])
def api():
    try:
        data = request.get_json()
        if int(decode(data['token'], data['q'])) in range(floor(time.time())-10, floor(time.time()+10)):
            return jsonify({'ok': True, 'text': data['text']})
        else:
            return jsonify({'ok': False, 'text': 'you are gay and you are so fukcing noob'})
    except:
        return jsonify({'ok': False, 'text': 'you are gay and you are so fukcing noob'})

app.run()
