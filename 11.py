def valid(c, col, sol, adj):
    return all(sol.get(n)!=col for n in adj[c])

def backtrack(countries, colors, adj, sol={}):
    if len(sol)==len(countries): return sol
    c=[x for x in countries if x not in sol][0]
    for col in colors:
        if valid(c,col,sol,adj):
            sol[c]=col
            if backtrack(countries,colors,adj,sol): return sol
            sol.pop(c)
    return None

# --- Input ---
countries=input("Countries: ").split()
adj={c:[] for c in countries}
print("Enter neighbors (u v), type 'done' to stop:")
while True:
    x=input()
    if x=="done": break
    u,v=x.split(); adj[u].append(v); adj[v].append(u)
colors=input("Colors: ").split()

print(backtrack(countries,colors,adj))
