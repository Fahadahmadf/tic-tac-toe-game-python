# Tic-Tac-Toe Game (Advanced Version)
# Author: Fahad Ahmad Fayaz
# Internship: Python Developer

import random

# Initialize scores
player_score = 0
computer_score = 0


# Function to create a new board
def new_board():
    return [" " for _ in range(9)]


# Function to print the board
def print_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")


# Function to check winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# Function to check draw
def check_draw(board):
    return " " not in board


# Player move
def player_move(board):
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if pos < 0 or pos > 8:
                print("Invalid position.")
            elif board[pos] != " ":
                print("Position already taken.")
            else:
                board[pos] = "X"
                break
        except ValueError:
            print("Enter a valid number.")


# Easy mode (random move)
def computer_easy(board):
    available = [i for i in range(9) if board[i] == " "]
    pos = random.choice(available)
    board[pos] = "O"
    print(f"Computer (Easy) choose {pos + 1}")


# Hard mode (try to win/block)
def computer_hard(board):
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                print(f"Computer (Hard) choose {i + 1}")
                return
            board[i] = " "

    # Try to block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = "O"
                print(f"Computer (Hard) choose {i + 1}")
                return
            board[i] = " "

    # Otherwise random
    computer_easy(board)


# Game function
def play_game():
    global player_score, computer_score

    board = new_board()

    print("\n🎮 New Game Started!")
    print_board(board)

    # Choose difficulty
    mode = input("Choose difficulty (Easy/Hard): ").lower()

    while True:
        # Player turn
        player_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("🎉 You win!...")
            player_score += 1
            break

        if check_draw(board):
            print("It's a draw!!!")
            break

        # Computer turn
        if mode == "hard":
            computer_hard(board)
        else:
            computer_easy(board)

        print_board(board)

        if check_winner(board, "O"):
            print("💻 Computer wins!")
            computer_score += 1
            break

        if check_draw(board):
            print("It's a draw!")
            break


# Main loop with replay option
while True:
    play_game()

    print(f"\nScore Details:\nYour Score: {player_score} | Computer's Score: {computer_score}")
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay in ["yes", "y"]:
            break   # continue game loop
    elif replay in ["no", "n"]:
            print("Thanks for playing! 👋")
            exit()
    else:
        print("Invalid input. Please enter yes or no.")