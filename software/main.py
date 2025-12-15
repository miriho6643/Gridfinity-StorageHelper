from controller import *

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def receive_data():
    data = request.json["message"]
    print("Von HTML erhalten:", data)

    antwort = f"Python hat erhalten: {data}"
    return jsonify({"response": antwort})

if __name__ == "__main__":
    app.run(debug=True)
