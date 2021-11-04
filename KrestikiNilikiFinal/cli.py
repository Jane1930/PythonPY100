from logic import initialization_field, is_empty_ceil, is_win, has_any_moves


def is_answer_right(player_move):   # функция определяющая очередность хода
    answers_base = ("да", "нет")
    while True:
        if player_move.lower() not in answers_base:
            player_move = str(input("Игрок Х ходит первым? (ответ да или нет): "))
        else:
            break
    return player_move


def char_player(answer_x, counter):    # функция символа игрока
    if (answer_x == "да" and counter % 2 != 0) or (answer_x == "нет" and counter % 2 == 0):
        return "X"
    elif (answer_x == "нет" and counter % 2 != 0) or (answer_x == "да" and counter % 2 == 0):
        return "O"


def change_player(answer_x, counter):   # функция смены игрока
    if (answer_x == "да" and counter % 2 != 0) or (answer_x == "нет" and counter % 2 == 0):
        return input("Игрок Х введите номер ячейки: ")
    elif (answer_x == "нет" and counter % 2 != 0) or (answer_x == "да" and counter % 2 == 0):
        return input("Игрок O введите номер ячейки: ")


def print_field(field):    # функция печати поля
    for row in field:
        print(*row)


def make_move(field, row_index, col_index, char):    # функция заполнения ячейки
    field[row_index][col_index] = char


def get_step(size=3):           # функция хода игрока, получение координат
    while True:
        char = char_player(answer_x, counter)
        position = change_player(answer_x, counter)
        if not position.isdigit():
            print(f"Игрок {char}, вы ввели не число. Введите число от 1 до 9: ")
            continue
        position_int = int(position)
        if not 1 <= position_int <= size * size:
            print("Вы ввели неверную координату. Введите число от 1 до 9: ")
            continue
        x, y = single_to_double_coord(position_int, size=3)
        if not is_empty_ceil(x, y, position, field):
            print("Ячейка занята. Выберите другую ячейку: ")
            continue
        return x, y


def single_to_double_coord(position, size=3):    # перевод координаты в двумерные
    coord = int(position) - 1
    row_index = coord // size
    col_index = coord % size
    return row_index, col_index


if __name__ == '__main__':
    print("""Перед вами игра 'Крестики-нолики'.
    Участвуют два игрока с именами Х и О.
    Для того, чтобы сделать ход, нужно каждому игроку в ячейке ввода поочередно
    указать значение от 1 до 9.
    После чего ход переходит другому игроку.
    Побеждает тот, кто быстрее заполнит своими символами, строку или столбец, или любую диагональ.""")
    player_move = str(input("Игрок Х ходит первым? (ответ да или нет): "))
    answer_x = is_answer_right(player_move)
    counter = 1
    field = initialization_field()
    print_field(field)
    while has_any_moves(field):
        char = char_player(answer_x, counter)
        x, y = get_step(size=3)
        make_move(field, x, y, char)
        if is_win(field, char):
            print(f"Выиграл игрок {char}")
            print_field(field)
            break
        print_field(field)
        if not has_any_moves(field):
            print("Ходы закончились. Ничья.")
            break
        counter += 1
