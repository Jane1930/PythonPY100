EMPTY_CEIL = "-"


def init_field(size: int =3) -> list:
    field = [
        [EMPTY_CEIL for _ in range(size)]
        for _ in range(size)
    ]

    return field


def set_ceil(field: list, row_index: int, col_index: int, player_symbol) -> None:
    field[row_index][col_index] = player_symbol


def get_ceil(field: list, row_index: int, col_index: int):
    return field[row_index][col_index]


def is_enpty_ceil(field: list, row_index: int, col_index: int) -> bool:
    # if field[row_index][col_index] == EMPTY_CEIL:
    #     return True
    # else:
    #     return False
    return True if field[row_index][col_index] == EMPTY_CEIL else False


def is_win(field: list, player_symbol) -> bool:
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
        ceil_3 = get_ceil(field, row_index=win_comb[1][0], col_index=win_comb[2][1])
        if ceil_1 == ceil_2 == ceil_3 == player_symbol:   # (ceil_1 == ceil_2) and (ceil_2 == ceil_3) and (ceil_2 != EMPTY_ceil)
            return True

    return False


def is_available_ceil(field: list) -> bool:  # возможность хода
    for row in field:
        for ceil in row:
            if ceil == EMPTY_CEIL:
                return True
    return False
