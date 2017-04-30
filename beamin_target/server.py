#!/usr/bin/env python3
import json
import os
import zipfile
from flask import Flask, Response, request
from .info_beamer_service import InfoBeamerService

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route("/info-beamer/start")
def start():
    app.config['ibs'].start()
    return Response("Starting")

@app.route("/info-beamer/stop")
def stop():
    app.config['ibs'].stop()
    return "stopping"

@app.route("/info-beamer/restarting")
def restart():
    app.config['ibs'].restart()
    return "restarting"

@app.route("/info-beamer/status")
def status():
    if app.config['ibs'].is_running():
        return "running"
    else:
        return "not running"

@app.route("/node/push", methods=['GET', 'POST'])
def receive_node():
    if request.method != 'POST':
        return Response('Accepts POST requests only')

    if 'node.zip' not in request.files:
        return Response('Expected node.zip')

    node_file = request.files['node.zip']
    node_file_upload_path = os.path.join(app.config['UPLOAD_FOLDER'], 'node.zip')
    node_file.save(node_file_upload_path)
    with zipfile.ZipFile(node_file_upload_path) as zipped_node:
        zipped_node.extractall(app.config['NODE_FOLDER'])

    return Response('Node received')


def main():
    config = json.load(open('config.json'))
    ibs = InfoBeamerService(config)
    app.config['ibs'] = ibs
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['NODE_FOLDER'] = 'node'
    app.config['DEBUG'] = True
    app.run(port=8907)


if __name__ == '__main__':
    main()
