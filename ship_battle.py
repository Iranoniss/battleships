import random


def create_board():
    board = []
    for i in range(10):
        board.append([""] * 10)
    return board

def print_board(board):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(10):
        row_str = chr(ord('А') + i) + " "
        for j in range(10):
            row_str += board[i][j] + " "
        print(row_str)

class Ship:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_coords(self):
        coords = []
        if self.start[0] == self.end[0]:
            for i in range(self.start[1], self.end[1]+1):
                coords.append((self.start[0], i))
        else:
            for i in range(self.start[0], self.end[0]+1):
                coords.append((i, self.start[1]))
        return coords

player_ships = [Ship((0,0), (0,2)), Ship((2,4), (5,4)), Ship((7,8), (9,8))]
computer_ships = [Ship((1,3), (3,3)), Ship((4,6), (4,8)), Ship((6,1), (6,3))]

def player_turn(board, computer_ships):
    print("Твоя очередь!!")
    while True:
        guess = input("Введите координаты в строку формы, столбец (например, 3,4):")
        guess = guess.split(",")
        row = int(guess[0]) - 1
        col = int(guess[1]) - 1

        if row < 0 or row > 9 or col < 0 or col > 9:
            print("Этого даже не существует))")
        elif board[row][col] !="":
            print("Ты уже стрелял сюда!")
        else:
            break
    if (row, col) in [ship_coord for ship in computer_ships for ship_coord in ship.get_coords()]:
        print("Хит!")
        board[row][col] = "O"
        for ship in computer_ships:
            if (row, col) in ship.get_coords():
                ship.get_coords().remove((row, col))
                if len(ship.get_coords()) == 0:
                    print("Ты потопил мой корабль, гад!!")
    else:
        print("Промазал!")
        board[row][col] = "X"

def computer_turn(board, player_ships):
    print("Ход ИИ((")
    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if board[row][col] !="":
            continue
        else:
            break

    if (row, col) in [ship_coord for ship in player_ships for ship_coord in ship.get_coords()]:
        print("ИИ попал в твой корабль!((")
        board[row][col] = "O"
        for ship in player_ships:
            if (row, col) in ship.get_coords():
                ship.get_coords().remove((row, col))
                if len(ship.get_coords()) == 0:
                    print("ИИ потопил ваш корабль((")
    else:
        print("ИИ промазал!)")
        board[row][col] = "X"

def play_game():
    player_board = create_board()
    computer_board = create_board()

    print("Давай поиграем!")
    print("Корабль игрока:")
    for ship in player_ships:
        for coord in ship.get_coords():
            player_board[coord[0]][coord[1]] = "S"
    print_board(player_board)

    while True:
        player_turn(player_board, computer_ships)
        print_board(player_board)
        if all(len(ship.get_coords()) == 0 for ship in computer_ships):
            print("Поздравляю ты крутышка!!!)))")
            break
        computer_turn(computer_board, player_ships)
        print_board(computer_board)
        if all(len(ship.get_coords()) == 0 for ship in player_ships):
            print("Сорян ИИ победил!(")
            break

play_game()
print_board()


