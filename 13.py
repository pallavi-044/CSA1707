def minimax(depth, node, max_turn, values, h):
    if depth == h:  # leaf node
        return values[node]
    if max_turn:
        return max(minimax(depth+1, node*2, False, values, h),
                   minimax(depth+1, node*2+1, False, values, h))
    else:
        return min(minimax(depth+1, node*2, True, values, h),
                   minimax(depth+1, node*2+1, True, values, h))

# --- Input ---
h = int(input("Enter height of game tree: "))
n = 2**h
print(f"Enter {n} leaf node values:")
values = list(map(int, input().split()))

# --- Run ---
best = minimax(0, 0, True, values, h)
print("Optimal value for Maximizer:", best)
