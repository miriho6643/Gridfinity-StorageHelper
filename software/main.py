from controller import *
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/button", methods=["POST"])
def button():
    button_name = request.json["name"]
    

    # hier kannst du später reagieren:
    # if button_name == "START": ...
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(debug=True)
    
