from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def send_html():
    return send_file("index.html")

@app.route("/<path:path>")
def send_json(path):
    return send_file(path)

app.run("0.0.0.0", port=8000, debug=True)