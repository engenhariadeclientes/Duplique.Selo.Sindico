import os

import requests
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

APPS_SCRIPT_URL = os.environ.get(
    "APPS_SCRIPT_URL",
    "https://script.google.com/macros/s/AKfycbx6PtMkJUEx0iYopPeQcJaV2YlDfdCshqpkZQ3fzSGqCNueVqMRfqPQ_3pXKhDoWznqNg/exec",
)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/submit-lead", methods=["POST"])
def submit_lead():
    dados = request.get_json(silent=True) or {}
    try:
        requests.post(APPS_SCRIPT_URL, json=dados, timeout=10)
    except requests.RequestException as err:
        print("Falha ao enviar lead para a planilha:", err)
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
