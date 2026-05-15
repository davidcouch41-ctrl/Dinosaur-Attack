from pathlib import Path

from flask import Flask, send_from_directory


ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=str(ROOT), static_url_path="")


@app.route("/")
def home():
    return send_from_directory(ROOT, "index.html")


@app.route("/<path:asset_path>")
def assets(asset_path: str):
    return send_from_directory(ROOT, asset_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
