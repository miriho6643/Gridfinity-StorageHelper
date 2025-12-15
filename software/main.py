from controller import *
import config
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        rows=config.GRID_ROWS,
        cols=config.GRID_COLS
    )

@app.route("/button", methods=["POST"])
def button():
    row = request.json["row"]
    col = request.json["col"]
    print(row, col)

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
