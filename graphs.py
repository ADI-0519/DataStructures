# Graphs can be supplied using array of edges, an adjacecency matrix, a class or a dictionary

n = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

# Adjacency matrix representation. Useful for dense graphs. Space complexity: O(V^2)
# Adjacency list representation. Useful for sparse graphs. Space complexity: O(V + E)
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

# Creating dictionary adjacency list

def edge_to_adj_list_dict(n, edges):
    adj_list = {i : [] for i in range(n)}

    for u,v in edges:
        adj_list[u].append(v)
        # If undirected graph, uncomment the next line
        # adj_list[v].append(u)

    return adj_list

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

# dfs via iteration time complexity: O(V + E), space complexity: O(V) Assumes graph is connected

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

    # If you want to handle disconnected graphs, uncomment the next lines
    # for i in range(len(graph)):
    #     if i not in seen:
    #         seen.add(i)
    #         stk.append(i)
    #        while stk: 
    #            node = stk.pop()
    #            print(node)        



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

            
# Performing level order BFS on graph
# In a graph, a level is the number of edges from the source node.

def level_order_bfs(matrix):

    rows, cols = len(matrix),len(matrix[0])
    seen = set()
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    q = deque([(0,0)])
    seen.add((0,0))

    levels = []

    while q:
        level_size = len(q)
        curr = []
        
        for i in range(level_size):
            r,c = q.popleft()
            curr.append((r,c))
            for x,y in directions:
                nr, nc = r + x, c + y
                if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] == 1 and (nr,nc) not in seen):
                    seen.add((nr,nc))
                    q.append((nr,nc))

        levels.append(curr)

    return levels


def count_connnected_components(graph):
    
    seen = set()
    components = 0

    def dfs(node):
        stk = [node]
        seen.add(node)
        while stk:
            curr = stk.pop()
            for neightbour in graph.get(curr, []):
                if neightbour not in seen:
                    seen.add(neightbour)
                    stk.append(neightbour)

    for item in graph:
        if item not in seen:
            components += 1
            dfs(item)


def cycle_check(graph):
    seen = set()
    
    def dfs(node, parent):
        stk = [(node, parent)]
        seen.add(node)

        while stk:
            item, curr_parent = stk.pop()

            for nei in graph.get(item, []):
                if nei not in seen:
                    seen.add(nei)
                    stk.append((nei, item))

                elif curr_parent != nei:
                    print("Cycle detected")
                    return True

        return False
    
    for node in graph:
        if node not in seen:
            if dfs(node, None):
                return True
    return False

def directed_cycle_check(graph):
    UNVISITED, VISITING, VISITED = 0, 1, 2

    
    for node in graph:
        graph[node] = (graph[node], UNVISITED)
    

def unique_paths(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    stk = [(0,0,0)]

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1 or len(grid) == 0:
        return 0

    target = (rows - 1, cols - 1)
    grid[0][0] = 1
    count = 0

    while stk:
        r,c, phase = stk.pop()

        # processing logic here

        if (r,c) == target:
            count += 1
            grid[r][c] = 0
            continue

        if phase == 0:
            # we are visiting the node for the first time
            stk.append((r,c,1))

        if phase == 1:
            # we are leaving the node after visiting all its neighbours
            grid[r][c] = 0
            continue

        for x, y in directions:
            nr, nc = r + x, c + y
            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0):
                stk.append((nr,nc, 0))
                grid[nr][nc] = 1
    
    return count

def djikstra(graph):
    