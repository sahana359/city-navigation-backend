import osmnx as ox
from dijkshtras import Dijkshtras

class CityLoader:
    def __init__(self, city_name: str):
        self.G = None
        self.dijkshtras = None
        self.load_city(city_name)

    def load_city(self, place_name: str):
        print(f"Downloading map data for {place_name}...")
        self.G = ox.graph_from_place(place_name, network_type="drive")
        print(f"Graph loaded: {len(self.G.nodes)} nodes, {len(self.G.edges)} edges")

        edges = []
        for src, dst, data in self.G.edges(data=True):
            weight = round(float(data.get("length", 1)), 4)
            name = data.get("name", "unknown")
            edges.append((src, dst, weight, name))

        self.dijkshtras = Dijkshtras(edges)

    def get_graph(self):
        return self.G

    def get_dijkshtras(self):
        return self.dijkshtras