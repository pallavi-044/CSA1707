def alphabeta(depth, node, max_turn, values, h, alpha, beta):
    if depth == h:  # leaf node
        return values[node]

    if max_turn:  # Maximizer's turn
        best = float("-inf")
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, False, values, h, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha: break  # prune
        return best
    else:  # Minimizer's turn
        best = float("inf")
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, True, values, h, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha: break  # prune
        return best

# --- Input ---
h = int(input("Enter height of game tree: "))
n = 2**h
print(f"Enter {n} leaf node values:")
values = list(map(int, input().split()))

# --- Run ---
result = alphabeta(0, 0, True, values, h, float("-inf"), float("inf"))
print("Optimal value for Maximizer:", result)
