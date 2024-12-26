def get_player_move():
    while True:
        try:
            position = int(input("Enter position (0-8): "))
            if 0 <= position <= 8:
                return position
            print("Please enter a number between 0 and 8.")
        except ValueError:
            print("Please enter a valid number.")