class Graph:
    
    def __init__(self):
        self.edges = {}

    def addEdge(self, src: int, dst: int) -> None:
        if not src in self.edges:
            self.edges[src] = []
        if not dst in self.edges:
            self.edges[dst] = []
        self.edges[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.edges and dst in self.edges[src]:
            self.edges[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        visited.add(src)
        queue = deque()
        queue.append(src)

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True

                for neighbour in self.edges[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)

        return False
