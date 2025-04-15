from flask import Flask, request

app = Flask(__name__)

@app.route("/departing/taxi", methods=['GET'])
def departing_taxi():
    plane_id = request.args.get("plane_id")
    return "Runway 69"

@app.route("/departing/takeoff", methods=['GET'])
def departing_takeoff():
    plane_id = request.args.get("plane_id")
    runway = request.args.get("runway")
    return "Not Cleared"

@app.route("/arriving/where", methods=['GET'])
def arriving_where():
    plane_id = request.args.get("plane_id")
    return "Runway 420"

@app.route("/arriving/clearance", methods=['GET'])
def arriving_clearance():
    plane_id = request.args.get("plane_id")
    runway = request.args.get("runway")
    return "Not Cleared"
