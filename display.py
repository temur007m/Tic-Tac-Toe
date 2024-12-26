def print_board(board):
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def print_board_with_positions():
    print("Positions:")
    for i in range(0, 9, 3):
        print(f" {i} | {i+1} | {i+2} ")
        if i < 6:
            print("-----------")