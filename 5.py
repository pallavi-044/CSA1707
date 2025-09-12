from collections import deque

def valid(m, c, side, total):
    ml, cl = (m, c)
    mr, cr = (total-m, total-c)
    if ml<0 or cl<0 or mr<0 or cr<0: return False
    if (ml and ml<cl) or (mr and mr<cr): return False
    return True

def bfs(total=3, boat=2):
    start, goal = (total,total,0), (0,0,1)
    q = deque([(start, [])])
    seen = {start}
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    while q:
        (m,c,side), path = q.popleft()
        if (m,c,side) == goal: return path
        for dm,dc in moves:
            if dm+dc>boat: continue
            if side==0: new=(m-dm,c-dc,1)
            else: new=(m+dm,c+dc,0)
            if valid(new[0],new[1],new[2],total) and new not in seen:
                seen.add(new)
                q.append((new, path+[new]))
    return None

# --- Run ---
n = int(input("Enter number of missionaries (and cannibals): "))
sol = bfs(n)
if sol:
    print("\nSolution found in", len(sol), "steps:")
    for i,s in enumerate(sol,1):
        print("Step",i,":",s)
else:
    print("No solution.")
