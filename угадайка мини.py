from random import *
def play_game():
    rand_nums = randint(1,100)
    attempts = 5
    print("Я загадал число в пределах от 1 до 100")
    print("У вас есть 5 попыток, чтобы его отгадать")
    print("После каждой неверной попытки, будет дана подсказка")
    print("Как только число угадано, или закончены попытки, игра подходит к концу")
    while attempts > 0:
        guess = int(input("Введите предположение"5))
        if guess > rand_nums:
            print("Слишком много")
        elif guess<rand_nums:
            print("Слишком мало")
        else:
            print(f'Поздравляю! Вы гений и угадали число {rand_nums}')
            break
        attempts -=1
        print(f"Осталось попыток\n{attempts}")
    if attempts == 0:
        print(f"Увы... \n Попытки испарились:/\nЗагаданное число = {rand_nums}")
def main():
    while True:
        play_game()
        print("Хотите сыграть ещё раз?(да = д; нет = н)")
        answer = input()
        if answer != 'д':
            print("Спасибо за игру!")
            break
if __name__ == "__main__":
    main()