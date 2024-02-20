import numpy as np
import random
# Размеры игрового поля
BOARD_SIZE = 4

# Возможные ходы
MOVES = ["w", "a", "s", "d"]


# Создание пустого игрового поля
def create_board():
    return np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

print(type(create_board()))
# Добавление случайного числа на пустую клетку
def add_random_number(board):
    while True:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)
        if board[x, y] == 0:
            board[x, y] = random.choice([2, 4])
            break


# Проверка, является ли игра законченной
def is_game_over(board):
    return not np.any(board == 0) and not is_move_possible(board)


# Проверка, возможен ли ход
def is_move_possible(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i, j] == 0:
                return True
            elif i > 0 and board[i, j] == board[i - 1, j]:
                return True
            elif j > 0 and board[i, j] == board[i, j - 1]:
                return True
    return False


# Выполнение хода
def make_move(board, move):
    if move == "w":
        for i in range(1, BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i, j] != 0:
                    k = i
                    while k > 0 and board[k - 1, j] == 0:
                        board[k - 1, j] = board[k, j]
                        board[k, j] = 0
                        k -= 1
                    if board[k, j] == board[k - 1, j]:
                        board[k - 1, j] *= 2
                        board[k, j] = 0
    elif move == "a":
        for j in range(1, BOARD_SIZE):
            for i in range(BOARD_SIZE):
                if board[i, j] != 0:
                    k = j
                    while k > 0 and board[i, k - 1] == 0:
                        board[i, k - 1] = board[i, k]
                        board[i, k] = 0
                        k -= 1
                    if board[i, k] == board[i, k - 1]:
                        board[i, k - 1] *= 2
                        board[i, k] = 0
    elif move == "s":
        for i in range(BOARD_SIZE - 2, -1, -1):
            for j in range(BOARD_SIZE):
                if board[i, j] != 0:
                    k = i
                    while k < BOARD_SIZE - 1 and board[k + 1, j] == 0:
                        board[k + 1, j] = board[k, j]
                        board[k, j] = 0
                        k += 1
                    if board[k, j] == board[k + 1, j]:
                        board[k + 1, j] *= 2
                        board[k, j] = 0
    elif move == "d":
        for j in range(BOARD_SIZE - 2, -1, -1):
            for i in range(BOARD_SIZE):
                if board[i, j] != 0:
                    k = j
                    while k < BOARD_SIZE - 1 and board[i, k + 1] == 0:
                        board[i, k + 1] = board[i, k]
                        board[i, k] = 0
                        k += 1
                    if board[i, k] == board[i, k + 1]:
                        board[i, k + 1] *= 2
                        board[i, k] = 0


# Печать игрового поля
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


# Основная функция игры
def play_game():
    board = create_board()
    add_random_number(board)
    add_random_number(board)

    while not is_game_over(board):
        print_board(board)
        move = input("Введите ход (w, a, s, d): ")
        if move in MOVES:
            make_move(board, move)
            add_random_number(board)
        else:
            print("Неверный ход")

    print("Игра окончена!")
    print_board(board)


if __name__ == "__main__":
    play_game()


#pip install numpy
