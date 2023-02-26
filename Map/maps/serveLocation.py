from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

import json 

def init_json():
    with open("loc.json", "w") as f:
        json.dump({
            "location": [87.31092, 22.32104]
        }, f)


init_json()



app = Flask(__name__)
api = Api(app)
CORS(app)

dummy_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [
                        87.31116,
                        22.32108 
                    ],
                    [
                        87.31092,
                        22.32104 
                    ],
                ]
            }
        }
    ]
}

class SeeUpdatedLocation(Resource):
    def get(self):
        with open("loc.json", "r") as f:
            data = json.load(f)
        print(data["location"])
        return data["location"]

class UpdateLocation(Resource):
    
    def post(self, lat, lon):
        with open("loc.json", "r") as f:
            data = json.load(f)
        data["location"] = [lon, lat]
        with open("loc.json", "w") as f:
            json.dump(data, f)
        return data["location"]

class GetLocation(Resource):
    def get(self):
        return dummy_geojson

api.add_resource(SeeUpdatedLocation, '/')
api.add_resource(UpdateLocation, '/update/<float:lat>/<float:lon>')
api.add_resource(GetLocation, '/location')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug=True)