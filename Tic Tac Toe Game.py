# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player or \
       board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'

    while True:
        print_board()

        # Get the player's move
        move = input("Enter the position (1-9): ")

        # Validate the move
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        index = int(move) - 1

        if board[index] != ' ':
            print("Position already taken. Please choose another position.")
            continue

        # Update the board
        board[index] = current_player

        # Check if the current player has won
        if check_winner(current_player):
            print_board()
            print("Player", current_player, "wins!")
            break

        # Check if the board is full
        if is_board_full():
            print_board()
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()

