__author__ = 'karnikamit'
from flask import jsonify, request, render_template
from routes import app
from Downloads.download import Download


@app.route('/try', methods=["POST"])
def api_try():
    data = request.json
    return jsonify(data)


@app.route('/get_file', methods=["POST", "GET"])
def download_file():
    path = request.form['path']
    do = Download(path)
    try:
        do.download_file()
        return jsonify({"response": "success", "msg": "file successfully downloaded."})
    except Exception, e:
        return jsonify({"response": "failure", "msg": str(e)})


@app.route("/Download", methods=["GET"])
def download_api():
    return render_template('download_form.html')


@app.route("/Upload", methods=["GET"])
def upload_api():
    return render_template('upload_form.html')
