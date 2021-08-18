import random
from math import ceil

print('Добро пожаловать в числовую угадайку')
print('Я загадал число от 1 до 100, сможешь угадать какое?')

def is_valid(number):
    # Проверка на то, что пользователь действительно введет число и в нужном диапазоне
    if number.isdigit() and 1 <= int(number) <= 101:
        return True
    else:
        return print('А может быть все-таки введем целое число от 1 до 100?')

def the_game():
    # Получаем случайное число из диапазона от 1 до 100
    random_number = random.randint(1, 100)
    # Число попыток пользователя
    tries_of_user = 0
    while True:
        user_guess = input('Введи свое число: ')
        if is_valid(user_guess):
            user_guess = ceil(int(user_guess))
            if user_guess < random_number:
                tries_of_user += 1
                print('Твое число меньше того, что я загадал. Попробуй еще раз..')
            if user_guess > random_number:
                tries_of_user += 1
                print('Твое число больше того, что я загадал. Попробуй еще раз..')
            if user_guess == random_number:
                print('Ух ты! Ты угадал мое число!', f'Попыток понадобилось -> {tries_of_user}')

the_game()
print('Еще увидимся!')