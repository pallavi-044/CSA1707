# 8 Puzzle Game (Simple Version with Win Check)

# Initial puzzle state
puzzle = [[1, 2, 3],
          [4, 0, 6],   # 0 = blank space
          [7, 5, 8]]

# Goal state
goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# Function to print puzzle
def print_puzzle(p):
    for row in p:
        print(row)
    print()

# Function to find position of blank (0)
def find_blank(p):
    for i in range(3):
        for j in range(3):
            if p[i][j] == 0:
                return i, j

# Move function
def move(p, direction):
    i, j = find_blank(p)
    if direction == "up" and i > 0:
        p[i][j], p[i-1][j] = p[i-1][j], p[i][j]
    elif direction == "down" and i < 2:
        p[i][j], p[i+1][j] = p[i+1][j], p[i][j]
    elif direction == "left" and j > 0:
        p[i][j], p[i][j-1] = p[i][j-1], p[i][j]
    elif direction == "right" and j < 2:
        p[i][j], p[i][j+1] = p[i][j+1], p[i][j]
    else:
        print("Invalid move!")

# Game loop
print("Initial Puzzle:")
print_puzzle(puzzle)

while True:
    if puzzle == goal:
        print("🎉 Puzzle Solved!")
        break
    direction = input("Move (up/down/left/right or quit): ")
    if direction == "quit":
        break
    move(puzzle, direction)
    print_puzzle(puzzle)
