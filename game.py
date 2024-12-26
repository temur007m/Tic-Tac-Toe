from board import Board
from display import print_board, print_board_with_positions
from input_handler import get_player_move

def play_game():
    board = Board()
    players = ["X", "O"]
    current_player = 0
    
    print("Welcome to Tic-Tac-Toe!")
    print_board_with_positions()
    print("\nUse these positions to make your move.\n")
    
    while True:
        print_board(board.board)
        player = players[current_player]
        print(f"\nPlayer {player}'s turn")
        
        position = get_player_move()
        if not board.make_move(position, player):
            print("Invalid move, try again.")
            continue
            
        if board.is_winner(player):
            print_board(board.board)
            print(f"\nPlayer {player} wins!")
            break
            
        if board.is_full():
            print_board(board.board)
            print("\nIt's a tie!")
            break
            
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_game()