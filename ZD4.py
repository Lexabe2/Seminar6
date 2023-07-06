import random


def training4(riddle: str, guesses: list[str], limit: int) -> str:
    count = 0
    guesses = list(map(lambda x: x.lower(), guesses))
    print(riddle)
    while count < limit:
        entry = input("Введите отгадку: ").lower()
        count += 1
        if entry in guesses:
            print(f"Вы отгадали с {count} попытки")
            break
        else:
            print(f"Не угадали осталось попыток {limit - count}")
    return 0


def puzzle_solut():
    dict_puzzle = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'],
                   'Висит груша - нельзя скушать': ['груша', 'игрушка',
                                                    'лампочка']}

    for key, values in dict_puzzle.items():
        training4(key, values, random.randint(1, 5))


_solutions = {}  # словарь protected (защищенный)
puzzle_dict = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'],
               'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}


def puzzle_solver(puzzle_text: str, tries: int):
    num = training4(puzzle_text, puzzle_dict[puzzle_text], tries)
    _solutions[puzzle_text] = [num, True if num else False]


def show_rez():
    for k, v in _solutions.items():
        print(k, v)
