#Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота

board = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_board():
    print(board[0],"|", end=" ")
    print(board[1],"|",end=" ")
    print(board[2])

    print(board[3], "|", end=" ")
    print(board[4], "|", end=" ")
    print(board[5])

    print(board[6],"|",  end=" ")
    print(board[7],"|",  end=" ")
    print(board[8])


def begin_step(step, symbol):
    ind = board.index(step)
    board[ind] = symbol

def result():
    win = ""

    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"

    return win

game_over = False
player1 = True

while game_over == False:

    print_board()

    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 'Х', ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 'O', ваш ход: "))

    begin_step(step, symbol)
    win = result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_board()
print("Победил", win)