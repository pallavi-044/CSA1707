from heapq import heappop, heappush

def a_star(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, node, path = heappop(pq)
        if node == goal: return path, g
        if node in visited: continue
        visited.add(node)
        for nbr,cost in graph[node]:
            if nbr not in visited:
                g2 = g + cost
                heappush(pq,(g2+h[nbr], g2, nbr, path+[nbr]))
    return None, float("inf")

# --- Input ---
n = int(input("No. of nodes: "))
graph = {input(f"Node {i+1} name: "): [] for i in range(n)}
m = int(input("No. of edges: "))
for _ in range(m):
    u,v,w = input("u v w: ").split()
    graph[u].append((v,int(w)))

h = {node:int(input(f"Heuristic of {node}: ")) for node in graph}
start = input("Start: ")
goal = input("Goal: ")

# --- Run ---
path,cost = a_star(graph,h,start,goal)
print("Path:", "->".join(path))
print("Cost:", cost)
