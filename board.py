class Board:
    def __init__(self):
        self.board = [" " for _ in range(9)]
    
    def make_move(self, position, player):
        if self.is_valid_move(position):
            self.board[position] = player
            return True
        return False
    
    def is_valid_move(self, position):
        return 0 <= position <= 8 and self.board[position] == " "
    
    def is_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if all(self.board[i + j] == player for j in range(3)):
                return True
        
        # Check columns
        for i in range(3):
            if all(self.board[i + j] == player for j in range(0, 9, 3)):
                return True
        
        # Check diagonals
        if all(self.board[i] == player for i in [0, 4, 8]):
            return True
        if all(self.board[i] == player for i in [2, 4, 6]):
            return True
        
        return False
    
    def is_full(self):
        return " " not in self.board