
class AdjMatrix:
    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([0 for _ in range(size)])
        self.size = size

    def __repr__(self):
        matrix = ''
        for row in self.matrix:
            for val in row:
                matrix += f'{val} '
            matrix += '\n'
        return matrix

    def __len__(self):
        return self.size

    def add_edge(self, v1, v2):
        if v1 == v2:
            return
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

    def __repr__(self):
        return repr(self.vertex)


class AdjList:
    def __init__(self, num):
        self.vertices = num
        self.graph = [] * self.vertices

    def __repr__(self):
        graph = ''
        for i in range(self.vertices):
            graph += f'Vertex: {i}'
            temp = self.graph[i]
            while temp:
                graph += f' -> {temp.vertex}'
                temp = temp.next
            graph += '\n'
        return graph

    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(visited)
    for next in graph[start] - visited:
        dfs(graph, next, visited)


def bfs(graph, root):
    from collections import deque
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex), end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


class Kosaraju:
    def __init__(self, vertex):
        from collections import defaultdict
        self.vertex = vertex
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        self.graph[s].append(d)

    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end=' ')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack.append(d)

    def transpose(self):
        g = Kosaraju(self.vertex)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def print_scc(self):
        stack = []
        visited_vertex = [False] * self.vertex

        for i in range(self.vertex):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * self.vertex

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print()


def adj_m():
    matr = AdjMatrix(5)
    print(matr)
    matr.add_edge(0, 1)
    print(matr)
    matr.add_edge(0, 2)
    print(matr)
    matr.add_edge(1, 2)
    print(matr)
    matr.add_edge(2, 0)
    print(matr)
    matr.remove_edge(0, 2)
    print(matr)
    matr.add_edge(2, 3)
    print(matr)


def adj_list():
    graph = AdjList(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    print(graph)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    print(graph)


def dfs_test():
    graph = {
        '0': {'1', '2'},
        '1': {'0', '3', '4'},
        '2': {'0'},
        '3': {'1'},
        '4': {'2', '3'}
    }
    dfs(graph, '0')


def bfs_test():
    graph = {
        0: [1, 2], 1: [2], 2: [3], 3: [1, 2]
    }
    bfs(graph, 0)


def scc_test():
    graph = Kosaraju(8)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 0)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.add_edge(6, 7)

    print("Strongly Connected Components:")
    graph.print_scc()


if __name__ == '__main__':
    adj_m()
    adj_list()
    dfs_test()
    bfs_test()
    scc_test()
