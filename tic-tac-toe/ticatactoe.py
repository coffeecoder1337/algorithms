'''
|1|2|3| 
|4|5|6| 
|7|8|9|
'''

winner_coordinates = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


game_map = [x for x in range(1, 10)]


x_moves = []
o_moves = []

winner = ''


def is_valid(n):
    try:
        n = int(n)
    except:
        return False
    else:
        if n not in range(1, 10):
            return False
    return True


def get_move():
    n = 0
    while not is_valid(n):
        n = input("Введите число от 1 до 9: ")
    return int(n)


def check_winner():
    for coords in winner_coordinates:
        if set(coords).issubset(set(x_moves)):
            return 'x'
        elif set(coords).issubset(set(o_moves)):
            return 'o'
        else:
            return False


def set_move(n, player):
    game_map[n] = player


def print_game_map(game_map):
    print('|' + '|'.join(str(x)+'|\n' if x % 3 == 0 else str(x) for x in game_map))

