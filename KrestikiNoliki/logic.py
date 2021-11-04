def initialization_field():    # функция задания поля
    size = 3
    field = [[(size * i) + j for j in range(1, size + 1)] for i in range(size)]
    return field


def get_ceil(field, row_index, col_index):
    return field[row_index][col_index]


def is_empty_ceil(x, y, position, field):    # функция проверки ячейки на занятость другим игроком
    return True if field[x][y] == int(position) else False


def has_any_moves(field):        # функция подсчета количества ходов
    base = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    counter_move = 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] in base:
                counter_move += 1
    return True if counter_move > 0 else False


def is_win(field, char):      # функция проверки на выигрыш
    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for win_comb in win_combinations:
        ceil_1 = get_ceil(field, row_index=win_comb[0][0], col_index=win_comb[0][1])
        ceil_2 = get_ceil(field, row_index=win_comb[1][0], col_index=win_comb[1][1])
        ceil_3 = get_ceil(field, row_index=win_comb[2][0], col_index=win_comb[2][1])
        if ceil_1 == ceil_2 == ceil_3 == char:
            return True

    return False

