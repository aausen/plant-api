"""REST Plant API"""

from logging import debug
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

plants = json.load(open(f'{app.root_path}/data/plants.json', 'r'))

    

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

@app.get("/plants/<plant_id>")
def get_single_plant(plant_id):
    
    return jsonify(plants[plant_id])

@app.post("/plants/<plant_id>")
def update_plant(plant_id):

    plant_to_update = plants[plant_id]


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)