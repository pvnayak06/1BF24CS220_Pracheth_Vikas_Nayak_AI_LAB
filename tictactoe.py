import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != '-' for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == '-']

def get_ai_move(board, ai_player, human_player):
    empty = get_empty_cells(board)


    for r, c in empty:
        board[r][c] = ai_player
        if check_win(board, ai_player):
            board[r][c] = '-'
            return (r, c)
        board[r][c] = '-'


    for r, c in empty:
        board[r][c] = human_player
        if check_win(board, human_player):
            board[r][c] = '-'
            return (r, c)
        board[r][c] = '-'

 
    if board[1][1] == '-':
        return (1, 1)

    return random.choice(empty)

def get_human_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player} - Enter row (0-2): "))
            col = int(input(f"Player {player} - Enter column (0-2): "))
        except ValueError:
            print("Invalid input. Enter numbers 0-2.")
            continue
        if row in range(3) and col in range(3) and board[row][col] == '-':
            return (row, col)
        print("Invalid move, try again.")

def tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]

    print("1. Human vs Human")
    print("2. Human vs AI")
    mode = input("Choose mode (1/2): ").strip()

    vs_ai = (mode == '2')
    human_player = 'X'
    ai_player = 'O'
    current_player = 'X'

    while True:
        print_board(board)

        if vs_ai and current_player == ai_player:
            print("AI is making a move...")
            row, col = get_ai_move(board, ai_player, human_player)
        else:
            row, col = get_human_move(board, current_player)

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()