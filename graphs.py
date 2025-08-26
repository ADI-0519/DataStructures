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