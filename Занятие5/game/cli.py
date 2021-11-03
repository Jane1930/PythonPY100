from random import randint
from logic import init_field, is_enpty_ceil, set_ceil, is_win, is_available_ceil


def get_step(field: list, player_symbol: str):
    size = 3
    while True:
        coord_str = input(f"Игрок {player_symbol} введите координату от 1 до 9: ")

        if not coord_str.isdigit():
            print("Вы ввели не число. Повторите ввод: ")
            continue    # перебросит на 6 строку

        coord = int(coord_str)
        if not 1 <= coord <= size * size:
            print("Вы ввели не вернуюю координату. Повторите ввод: ")
            continue

        x, y = single_to_double_coord(coord, size)
        if not is_enpty_ceil(field, x, y):
            print("Ячейка занятаю Повторите ввод: ")
            continue
        break
    return x, y     # или return в цикле while без break. Такая комбинация остановит цикл и вернет результат


def single_to_double_coord(coord: int, size: int) -> tuple[int, int]: # используем квадратные скобки для аннотации типов
    coord = coord - 1
    #coord = -coord
    row_index = coord // size
    col_index = coord % size

    return  row_index, col_index


def print_field(field: list):
    for row in field:
        for ceil in row:
            print(ceil, end=" ")
        print()


def player_step(field, player_symbol):
    x, y = get_step(field, player_symbol)
    set_ceil(field, x, y, player_symbol)
    print_field(field)


def first_player_step(field, player_symbol):
    size = 3
    while True:
        random_ceil_index = randint(1, size * size)
        x, y = single_to_double_coord(random_ceil_index)
        if is_enpty_ceil(field, x, y):
            set_ceil(field, x, y, player_symbol)
            break
    print_field(field)


def second_player_step(field, player_symbol):
    x, y = get_step(field, player_symbol)
    set_ceil(field, x, y, player_symbol)
    print_field(field)


def is_win_cli(field, player_symbol):
    if is_win(field):
        print(...)




def main():
    field = init_field()
    print_field(field)
    first_player, second_player = "X", "O"
    while True:
        first_player_step(field, first_player)
        if is_win(field, first_player):
            print(f"Выиграл игрок {first_player}")
            break

        if not is_available_ceil(field):
            print("Ходы закончились. Ничья")
            break

        second_player_step(field, second_player)
        if is_win(field, second_player):
            print(f"Выиграл игрок {second_player}")
            break

        if not is_available_ceil(field):
            print("Ходы закончились. Ничья")



if __name__ == "__main__":
    main()