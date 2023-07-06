import random


def training2(min_: int, max_: int, limit: int) -> bool:
    num = random.randint(min_, max_)
    count = 0
    while count != limit:
        entry = int(input("Введите число: "))
        count += 1
        print(f"Осталось попыток {limit - count}")
        if count >= limit:
            print(False)
            break
        if entry < num:
            print("Число больше")
        elif entry == num:
            print(True)
            break
        elif entry > num:
            print("Число меньше")


if __name__ == '__main__':
    training1(1, 100, 10)
