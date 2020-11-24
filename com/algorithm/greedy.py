
class FordF:
    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)

    def bfs(self, s, t, parent):
        visited = [False] * self.rows
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for i, val in enumerate(self.graph[u]):
                if visited[i] is False and val > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = u
        return True if visited[t] else False

    def max_flow(self, src, t):
        parent = [-1] * self.rows
        max_flow = 0
        while self.bfs(src, t, parent):
            path_flow = float('Inf')
            s = t
            while s != src:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = t
            while v != src:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


def ford_test():
    graph = [
        [0, 8, 0, 0, 3, 0],
        [0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 7, 2],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 7, 4, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    s, t = 0, 5
    ford = FordF(graph)
    print(f'Max Flow: {ford.max_flow(s, t)}')


def dijkstra(vertices, edges):
    from sys import maxsize
    num = len(vertices[0])
    visited_distance = [[0, 0]]
    for i in range(num - 1):
        visited_distance.append([0, maxsize])
    for vertex in range(num):
        to_visit = to_be_visited(num, visited_distance)
        for neighbor in range(num):
            if vertices[to_visit][neighbor] == 1 and visited_distance[neighbor][0] == 0:
                new_dist = visited_distance[to_visit][1] + edges[to_visit][neighbor]
                if visited_distance[neighbor][1] > new_dist:
                    visited_distance[neighbor][1] = new_dist
            visited_distance[to_visit][0] = 1
    i = 0
    for dist in visited_distance:
        print(f"Distance of {chr(ord('a') + i)} from source vertex: {dist[1]}")
        i += 1


def to_be_visited(n, visited):
    v = -10
    for i in range(n):
        if visited[i][0] == 0 and (v < 0 or visited[i][1] <= visited[v][1]):
            v = i
    return v


def dijkstra_test():
    vertices = [
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0]
    ]
    edges = [
        [0, 0, 1, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 3, 0],
        [1, 2, 0, 1, 3, 0, 0],
        [2, 0, 1, 0, 0, 0, 1],
        [0, 0, 3, 0, 0, 2, 0],
        [0, 3, 0, 0, 2, 0, 1],
        [0, 0, 0, 1, 0, 1, 0]
    ]
    dijkstra(vertices, edges)


class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            print(f'{u} - {v} : {weight}')


def kruskal_test():
    g = Kruskal(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 2, 4)
    g.add_edge(4, 3, 3)
    g.add_edge(5, 2, 2)
    g.add_edge(5, 4, 3)
    g.kruskal()


def prim(graph, vertices):
    inf = 9999999
    selected = [0] * vertices
    no_edge = 0
    selected[0] = True
    print('Edge : Weight')
    while no_edge < vertices - 1:
        minimum = inf
        x, y = 0, 0
        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if (not selected[j]) and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j
        print(f'{x} - {y} : {graph[x][y]}')
        selected[y] = True
        no_edge += 1


def prim_test():
    vertices = 5
    graph = [
        [0,  9,  75,  0,  0],
        [9,  0,  95, 19, 42],
        [75, 95,  0, 51, 66],
        [0,  19, 51,  0, 31],
        [0,  42, 66, 31,  0]
    ]
    prim(graph, vertices)


class BellFord:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print(self, dist):
        print('Vertex Distance from Source')
        for i in range(self.vertices):
            print(f'{i}\t{dist[i]}')

    def bellman_ford(self, src):
        dist = [float('Inf')] * self.vertices
        dist[src] = 0
        for _ in range(self.vertices - 1):
            for s, d, w in self.graph:
                if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        for s, d, w in self.graph:
            if dist[s] != float('Inf') and dist[s] + w < dist[d]:
                print('Graph contains negative weight cycle')
                return
        self.print(dist)


def bell_test():
    graph = BellFord(5)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 1, 6)
    graph.add_edge(3, 2, 2)

    graph.bellman_ford(0)


if __name__ == '__main__':
    ford_test()
    dijkstra_test()
    kruskal_test()
    prim_test()
    bell_test()
