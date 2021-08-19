import random
from math import ceil

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
    flag = True

    while flag:
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
                new_game()
                flag = False

# Новая игра
def new_game():
    question = input('Хочешь сыграть еще раз? Напиши да или нет -> ')
    flag = True
    while flag:
        if question.lower() == 'да':
            the_game()
        elif question.lower() == 'нет':
            return print('Еще увидимся!')
            flag = False
        else:
            question = input("Хитрюга, но меня не проведешь! Все же введи 'да' или 'нет' -> ")
           
print('Добро пожаловать в числовую угадайку')
print('Я загадал число от 1 до 100, сможешь угадать какое?')

the_game()