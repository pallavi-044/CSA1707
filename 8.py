# Depth First Search (DFS) using recursion

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")   # process the current node
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS
print("DFS Traversal starting from A:")
dfs(graph, 'A')
