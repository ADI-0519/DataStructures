# Graphs can be supplied using array of edges, an adjacecency matrix, a class or a dictionary

n = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

# Adjacency matrix representation
def edge_to_adj_matrix(n, edges):
    adj_matrix = [[0 for i in range(n)] for j in range(n)]

    for edge in edges:
        u, v = edge
        adj_matrix[u][v] = 1
        # If undirected graph, uncomment the next line
        # adj_matrix[v][u] = 1  

    return adj_matrix

print(edge_to_adj_matrix(n, A))


# Converting edge array to adjacency list
def edge_to_adj_list(n, edges):
    adj_list = [[] for i in range(n)]

    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        # If undirected graph, uncomment the next line
        # adj_list[v].append(u)  

    return adj_list

print(edge_to_adj_list(n, A))

# Converting edge array to adjacency list using defaultdict
from collections import defaultdict
def edge_to_adj_list_defaultdict(n, edges):
    adj_list = defaultdict(list)

    for u,v in edges:
        adj_list[u].append(v)
        # If undirected graph, uncomment the next line
        # adj_list[v].append(u)  

    return adj_list


print(edge_to_adj_list_defaultdict(n, A))


# DFS with recursion

def dfs(source, graph):
    
    def dfs_recursive(node):
        print(node)
        for neightbour in graph[node]:
            if neightbour not in seen:
                seen.add(neightbour)
                dfs_recursive(neightbour)
    
    
    
    seen = set()
    seen.add(source)
    dfs_recursive(source)


dfs(0, edge_to_adj_list_defaultdict(n, A))

# dfs via iteration time complexity: O(V + E), space complexity: O(V)

def dfs_iterative(source, graph):

    seen = set()
    seen.add(source)
    stk = [source]
    

    while stk:
        node = stk.pop()
        print(node)
        for neightbour in graph[node]:
            if neightbour not in seen:
                seen.add(neightbour)
                stk.append(neightbour)



dfs_iterative(0, edge_to_adj_list_defaultdict(n, A))

# BFS via iterative time complexity: O(V + E), space complexity: O(V)
from collections import deque

def bfs_iterative(source, graph):

    seen = set()
    seen.add(source)
    q = deque([source])

    while q:
        node = q.popleft()
        print(node)
        for neightbour in graph[node]:
            if neightbour not in seen:
                seen.add(neightbour)
                q.append(neightbour)

print(bfs_iterative(0, edge_to_adj_list_defaultdict(n, A)))

# Graphs can also be represented using a class

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # If undirected graph, uncomment the next line
        # self.graph[v].append(u)  

    def get_graph(self):
        return self.graph

g = Graph()
g.add_edge(0,1)

# There can also be matrix graph representation where the matrix is the graph.
# Each cell is a node and the edges are the adjacent cells.

matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

def matrix_dfs(mat):
    seen = set()
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    rows, cols = len(mat), len(mat[0])

    def dfs(r,c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or mat[r][c] == 0):
            return
        
        seen.add((r,c))
        print((r,c))

        for dr, dc in directions:
            dfs(r + dr, c + dc)

# Iterative DFS for matrix

def dfs(matrix):
    rows, cols = len(matrix),len(matrix[0])
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    stk = [(0,0)]

    seen = set()
    seen.add((0,0))

    while stk:
        r,c = stk.pop()
        print((r,c))

        for x,y in directions:
            nr, nc = r + x, c + y
            if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr,nc) in seen or matrix[nr][nc] == 0):
                continue

            seen.add((nr,nc))
            stk.append((nr,nc))

# Iterative BFS for matrix

def bfs(matrix):
    rows, cols = len(matrix),len(matrix[0])
    seen = set()
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    q = deque([(0,0)])
    seen.add((0,0))

    while q:
        r,c = q.popleft()
        print((r,c))

        # adding neighbours

        for x,y in directions:
            nr, nc = r + x, c + y
            if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1 and (nr,nc) not in seen):
                seen.add((nr,nc))
                q.append((nr,nc))

            

