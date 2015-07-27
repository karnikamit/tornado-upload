__author__ = 'karnikamit'
from flask import jsonify, request, render_template
from routes import app
from Downloads.download import Download

@app.route('/try', methods=["GET"])
def app_try():
    return jsonify({"response": "success"})

@app.route('/Download', methods=["POST", "GET"])
def download_file():
    path = request.json
    do = Download(path)
    try:
        do.download_file()
        return jsonify({"response": "success"})
    except Exception, e:
        return jsonify({"response": "failure", "msg": str(e)})