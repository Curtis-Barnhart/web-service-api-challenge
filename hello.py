from flask import Flask, request
from random import choice, randrange

runways: list[int] = [42, 43, 62, 179, 180]
takeoffs: dict[int, int]
landings: dict[int, int]
secret_runway: int = -2
app = Flask(__name__)

@app.route("/departing/taxi", methods=['GET'])
def departing_taxi():
    runway_choice: int
    try:
        plane_id: int = int(request.args.get("plane_id"))
    except:
        return "Bad plane_id value"
    if randrange(0, 100) == 0:
        runway_choice = secret_runway
    elif plane_id < 2000:
        runway_choice = choice(runways[:-2])
    else:
        runway_choice = choice(runways)
    takeoffs[plane_id] = runway_choice
    return "Runway {:d}".format(runway_choice)


@app.route("/departing/takeoff", methods=['GET'])
def departing_takeoff():
    try:
        plane_id = int(request.args.get("plane_id"))
    except:
        return "Bad plane_id value"
    try:
        runway = int(request.args.get("runway"))
    except:
        return "Bad runway value"

    if runway not in runways:
        return "Nonexistent runway"
    if takeoffs[plane_id] != runway:
        return "Not cleared"
    return "Cleared"


@app.route("/arriving/where", methods=['GET'])
def arriving_where():
    runway_choice: int
    try:
        plane_id: int = int(request.args.get("plane_id"))
    except:
        return "Bad plane_id value"
    if randrange(0, 100) == 0:
        runway_choice = secret_runway
    elif plane_id < 2000:
        runway_choice = choice(runways[:-2])
    else:
        runway_choice = choice(runways)
    landings[plane_id] = runway_choice
    return "Runway {:d}".format(runway_choice)

@app.route("/arriving/clearance", methods=['GET'])
def arriving_clearance():
    try:
        plane_id = int(request.args.get("plane_id"))
    except:
        return "Bad plane_id value"
    try:
        runway = int(request.args.get("runway"))
    except:
        return "Bad runway value"

    if runway not in runways:
        return "Nonexistent runway"
    if landings[plane_id] != runway:
        return "Not cleared"
    return "Cleared"
