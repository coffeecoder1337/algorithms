'''
|_|_|_| 
|_|_|_| 
|_|_|_|
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

x_moves = []
o_moves = []


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
