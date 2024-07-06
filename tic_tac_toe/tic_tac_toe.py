import random
import sys


def create_tic_tac_toe_board():
    return [['' for _ in range(3)] for _ in range(3)]


def display_board(board):
    for row in board:
        print(row)


def board_cell_is_empty(board, x, y):
    if board[x][y] == '':
        return True
    return False


def get_user_move(board):
    while True:
        try:
            user_input = input(
                'Place your move as matrix coordinates (x,y): ')
            if ',' not in user_input:
                raise ValueError
            x, y = user_input.split(',')

            x, y = int(x), int(y)
            if x and y > 2:
                print('Board size is 3x3.')
                raise ValueError

            if not board_cell_is_empty(board, x, y):
                display_board(board)
                raise ValueError

        except ValueError:
            print(
                'Invalid input!')
            continue
        return x, y


def get_computer_move(board):
    while True:
        x, y = (random.randint(0, 2), random.randint(0, 2))

        if board_cell_is_empty(board, x, y):
            return x, y


def input_move_into_board(board, x, y, input_value):
    board[x][y] = input_value
    return board


def check_winner(board, player_value):
    player = "User" if player_value == "X" else "Computer"

    board_length = len(board)

    # Check rows and columns
    for i in range(board_length):
        if all(board[i][j] == player_value for j in range(board_length)) or all(board[j][i] == player_value for j in range(board_length)):
            display_board(board)
            sys.exit(f'{player} wins!')

    # Check diagonals
    if all(board[i][i] == player_value for i in range(board_length)) or all(board[i][board_length - i - 1] == player_value for i in range(board_length)):
        display_board(board)
        sys.exit(f'{player} wins!')

    return False


def user_turn(board):
    user_move = get_user_move(board)
    board = input_move_into_board(
        board, *user_move, 'X')

    return board


def computer_turn(board):
    user_move = get_computer_move(board)
    board = input_move_into_board(
        board, *user_move, 'O')

    return board


def game_loop(board):
    board = user_turn(board)
    for _ in range(4):
        board = computer_turn(board)
        check_winner(board, 'O')
        display_board(board)

        board = user_turn(board)
        check_winner(board, 'X')
    sys.exit('Tie!')


def main():
    '''
    1. tic_tac_toe board matrix 3x3 creation
    2. Game loop finish when there is a winner or a tie
        2.1 Input from user
        2.2 Computer random move or make it play optimally
        2.3 Display board
        2.4 Declare winner or tie and display board and exit
    '''
    print('Welcome to Tic Tac Toe! Board size 3x3.')

    board = create_tic_tac_toe_board()
    display_board(board)

    game_loop(board)


if __name__ == '__main__':
    main()
