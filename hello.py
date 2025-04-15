from flask import Flask, request
from random import choice, randrange

runways: list[int] = [ 42, 43, 62, 179, 180]
secret_runway: int = -2
app = Flask(__name__)

@app.route("/departing/taxi", methods=['GET'])
def departing_taxi():
    runway_choice: int
    plane_id = request.args.get("plane_id")
    try:
        plane_int: int = int(plane_id)
    except:
        return "Bad plane_id value"
    if randrange(0, 100) == 0:
        runway_choice = secret_runway
    runway_choice = choice(runways)
    return "Runway {:d}".format(runway_choice)

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
