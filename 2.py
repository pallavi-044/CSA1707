def solve_n_queens(n):
    def can_place(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if can_place(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board)

    result = []
    place_queens(n, 0, [-1]*n)
    return [["."i + "Q" + "."(n-i-1) for i in sol] for sol in result]

# Example usage
n = 8
solutions = solve_n_queens(n)
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()
