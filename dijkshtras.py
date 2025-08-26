import heapq

class Dijkshtras:
    def __init__(self, edges):
        self.graph = self.buildAdjList(edges)
    
    def buildAdjList(self, edges):
        adjList = {}
        for s, d, w, p in edges:
            if s not in adjList:
                adjList[s] = []
            adjList[s].append((w, p, d))
        return adjList

    def findShortestPath(self, src, dest):
        dist = 0
        minHeap = [(0, [], src)]
        visited = {}
        path = []
        while minHeap:
            w, p, n = heapq.heappop(minHeap)
            if n in visited:
                continue
            visited[n] = w
            if n == dest:
                processed_path = self.process_path(p)
                return {"distance": round(w, 4), "path": processed_path}
            if n not in self.graph:
                continue
            for neighWeight, path, neigh in self.graph[n]:
                if neigh not in visited:
                    updatedPath = p + [path]
                    heapq.heappush(minHeap, (w+neighWeight, updatedPath, neigh))
        return {"distance": 0, "path": []}

    def process_path(self, path):
        processed_path = []
        n = len(path)
        i = 0
        while i < n:
            if path[i] == 'unknown':
                i += 1
                continue
            processed_path.append(path[i])
            while i + 1 < n and path[i] == path[i + 1]:
                i += 1
            i += 1
        return processed_path