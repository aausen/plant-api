"""REST Plant API"""

from logging import debug
from flask import Flask, request, jsonify

app = Flask(__name__)

plants = [ 
    {"id": 1, "name": "Ficus", "schedule": 2, "tips": "Lots of light, lots of water"},
    {"id": 2, "name": "Lime Tree", "schedule": 4, "tips": "Lots of light, lots of water"},
    {"id": 3, "name": "Aloe", "schedule": 14, "tips": "Medium light, light water"},
]

def _find_next_id():
    return max(plant["id"] for plant in plants) + 1

@app.get("/plants")
def get_plants():
    return jsonify(plants)

@app.post("/plants")
def add_plant():
    if request.is_json:
        plant = request.get_json
        plant["id"] = _find_next_id()
        plants.append(plant)
        return plant, 201
    return {error: "Request must be in JSON"}, 415

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)