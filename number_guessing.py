# -*- coding: utf-8 -*-
"""
Игра «Угадай число».

Компьютер загадывает число от 1 до 100, а ты пытаешься его угадать.
После каждой попытки игра подсказывает: больше или меньше загаданного.
"""

import random

MAX_ATTEMPTS = 10  # максимальное количество попыток


def play_round() -> bool:
    """Один раунд игры. Возвращает True, если игрок угадал."""
    secret = random.randint(1, 100)
    print("\nЯ загадал число от 1 до 100. Попробуй угадать!")

    attempt = 0
    while attempt < MAX_ATTEMPTS:
        user_input = input(f"Попытка {attempt + 1} из {MAX_ATTEMPTS}: ")
        attempt += 1

        # Проверяем, что ввели число (попытка не засчитывается)
        if not user_input.lstrip("-").isdigit():
            print("Это не число! Попробуй ещё раз.")
            attempt -= 1
            continue

        guess = int(user_input)

        if guess == secret:
            print(f"Ура! Ты угадал за {attempt} попыток! 🎉")
            return True
        elif guess < secret:
            print("Загаданное число БОЛЬШЕ.")
        else:
            print("Загаданное число МЕНЬШЕ.")

    print(f"Увы, попытки закончились. Я загадал число {secret}.")
    return False


def main():
    print("Добро пожаловать в игру «Угадай число»!")
    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        again = input("Сыграем ещё раз? (д/н): ").lower()
        if again not in ("д", "да", "y", "yes"):
            break

    print(f"\nСпасибо за игру! Ты угадал {wins} из {rounds} раз. До встречи!")


if __name__ == "__main__":
    main()
