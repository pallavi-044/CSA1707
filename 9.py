import itertools

def tsp(graph, start):
    nodes = list(range(len(graph)))
    nodes.remove(start)
    min_path = None
    min_cost = float("inf")

    for perm in itertools.permutations(nodes):
        path = [start] + list(perm) + [start]
        cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_path, min_cost

# --- Input ---
n = int(input("Enter number of cities: "))
graph = []
print("Enter distance matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting city (0 to n-1): "))

# --- Solve ---
path, cost = tsp(graph, start)

# --- Output ---
print("\nOptimal Path:", " -> ".join(map(str, path)))
print("Minimum Cost:", cost)
