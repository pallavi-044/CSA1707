def show(b):
    for r in b: print(" | ".join(r)); print("-"*5)

def win(b,p):
    return any(all(b[i][j]==p for j in range(3)) for i in range(3)) or \
           any(all(b[j][i]==p for j in range(3)) for i in range(3)) or \
           all(b[i][i]==p for i in range(3)) or \
           all(b[i][2-i]==p for i in range(3))

board=[[" "]*3 for _ in range(3)]
players=["X","O"]; turn=0

for _ in range(9):
    show(board)
    r,c=map(int,input(f"Player {players[turn]} row col (0-2): ").split())
    if board[r][c]!=" ":
        print("Spot taken! Try again."); continue
    board[r][c]=players[turn]
    if win(board,players[turn]):
        show(board); print("Player",players[turn],"wins!"); break
    turn=1-turn
else:
    show(board); print("Draw!")
