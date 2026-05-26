# ==========================================
#        TIC TAC TOE WITH AI (MINIMAX)
# ==========================================

import math

# Game board
board = [" " for i in range(9)]


# Function to print board
def print_board():

    print()

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")

    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")

    print(board[6] + " | " + board[7] + " | " + board[8])

    print()


# Function to check winner
def check_winner(player):

    win_positions = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]

    ]

    for position in win_positions:

        if board[position[0]] == player and \
           board[position[1]] == player and \
           board[position[2]] == player:

            return True

    return False


# Function to check draw
def check_draw():

    return " " not in board


# Function to get empty positions
def empty_positions():

    positions = []

    for i in range(9):

        if board[i] == " ":
            positions.append(i)

    return positions


# Minimax algorithm
def minimax(is_maximizing):

    # AI wins
    if check_winner("O"):
        return 1

    # Human wins
    if check_winner("X"):
        return -1

    # Draw
    if check_draw():
        return 0

    # AI turn
    if is_maximizing:

        best_score = -math.inf

        for position in empty_positions():

            board[position] = "O"

            score = minimax(False)

            board[position] = " "

            if score > best_score:
                best_score = score

        return best_score

    # Human turn
    else:

        best_score = math.inf

        for position in empty_positions():

            board[position] = "X"

            score = minimax(True)

            board[position] = " "

            if score < best_score:
                best_score = score

        return best_score


# AI move function
def ai_move():

    best_score = -math.inf
    best_move = 0

    for position in empty_positions():

        board[position] = "O"

        score = minimax(False)

        board[position] = " "

        if score > best_score:

            best_score = score
            best_move = position

    board[best_move] = "O"


# Player move function
def player_move():

    while True:

        try:

            move = int(input("Enter your move (1-9): ")) - 1

            if move >= 0 and move <= 8 and board[move] == " ":

                board[move] = "X"
                break

            else:
                print("Invalid move. Try again.")

        except:
            print("Please enter a number between 1 and 9.")


# Main game loop
print("===================================")
print("                 TIC TAC TOE WITH AI                      ")
print("===================================")

print("\nYou are X")
print("AI is O")

print("\nBoard positions are:")

print("""
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
""")


while True:

    # Print board
    print_board()

    # Player move
    player_move()

    # Check if player wins
    if check_winner("X"):

        print_board()

        print("🎉 Congratulations! You won.")
        break

    # Check draw
    if check_draw():

        print_board()

        print("🤝 Match Draw.")
        break

    # AI move
    print("\nAI is making a move...\n")

    ai_move()

    # Check AI win
    if check_winner("O"):

        print_board()

        print("😎 AI wins.")
        break

    # Check draw
    if check_draw():

        print_board()

        print("🤝 Match Draw.")
        break