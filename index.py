import os
import time

def print_board(board, x_wins, o_wins, winning_combo=None):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\nScores:")
    print(f"X: {x_wins}   O: {o_wins}\n")

def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return condition
    return None

def check_tie(board):
    return all(space != ' ' for space in board)

def check_win_move(board, player):
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            if check_win(board, player):
                board[i] = ' '
                return i
            board[i] = ' '
    return None

def best_move(board, player):
    win_move = check_win_move(board, player)
    if win_move is not None:
        return win_move

    opponent = 'O' if player == 'X' else 'X'
    block_move = check_win_move(board, opponent)
    if block_move is not None:
        return block_move

    if board[4] == ' ':
        return 4  # Prefer center

    for i in [0, 2, 6, 8]:  # Prioritize corners
        if board[i] == ' ':
            return i

    for i in range(9):
        if board[i] == ' ':
            return i

def play_game():
    x_wins = 0
    o_wins = 0

    while True:
        board = [' '] * 9
        current_player = 'X'

        while True:
            print_board(board, x_wins, o_wins)

            if current_player == 'X':  # Player's turn
                while True:
                    try:
                        move = int(input(f"Choose a spot (1-9): ")) - 1
                        if 0 <= move <= 8 and board[move] == ' ':
                            break
                        print("Invalid move. Please choose an empty spot from 1 to 9.")
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 9.")

            else:  # Computer's turn
                time.sleep(0.75)
                move = best_move(board, current_player)

            board[move] = current_player

            winning_combo = check_win(board, current_player)
            if winning_combo:
                print_board(board, x_wins, o_wins, winning_combo)
                print(f"\nPlayer {current_player} wins!")
                if current_player == 'X':
                    x_wins += 1
                else:
                    o_wins += 1
                break

            if check_tie(board):
                print_board(board, x_wins, o_wins)
                print("\nIt's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()
