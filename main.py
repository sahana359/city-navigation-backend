import osmnx as ox
from dijkshtras import Dijkshtras
from flask import Flask, jsonify, request
from flask_cors import CORS
from city_loader import CityLoader
app = Flask(__name__)
CORS(app)

city_loader = CityLoader("Boston, Massachusetts, USA")

@app.route("/shortest-distance", methods = ["POST"])
def get_shortest_distance():
    data = request.json
    start_address = data.get("start")
    end_address = data.get("end")

    if not start_address or not end_address:
        return {"error": "Please provide both 'start' and 'end' addresses."}
    G = city_loader.get_graph()
    dijkshtras = city_loader.get_dijkshtras()
    if not G or not dijkshtras:
        return {"error": "City graph or Dijkshtras not loaded."}

    start_point = ox.geocode(start_address)
    end_point = ox.geocode(end_address)
    start_node = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
    end_node = ox.distance.nearest_nodes(G, end_point[1], end_point[0])
    res = dijkshtras.findShortestPath(start_node, end_node)
    return jsonify(res)



if __name__ == "__main__":
    app.run(debug = True, port = 5000)