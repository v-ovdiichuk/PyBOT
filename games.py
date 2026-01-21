import random
from art import tprint
from colorama import Fore, Style, init
from time import sleep
from tqdm import tqdm
import emoji

def play_rps():
    """Гра Камінь, ножиці, папір"""
    options = ["камінь", " ножиці", "папір"]
    print(f"\n{Fore.CYAN}--- ГРА: Камінь, Ножиці, Папір ---")
    while True:
        user_choice = input(
            "Ваш вибір (камінь, ножиці, папір) або 'вихід' для завершення: ").lower()

        if user_choice == "вихід":
            break

        if user_choice not in options:
            print(Fore.RED + "Будь ласка, введіть правильне слово!")
            continue
        bot_choice = random.choice(options)
        print(f"Бот обрав: {Fore.YELLOW}{bot_choice}")

        if user_choice == bot_choice:
            print(Fore.BLUE + "Нічія!")
        elif (user_choice == "камінь" and bot_choice == "ножиці") or \
            (user_choice == "ножиці" and bot_choice == "папір") or \
                (user_choice == "папір" and bot_choice == "камінь"):
            print(Fore.GREEN + "Ви перемогли!")
        else:
            print(Fore.RED + "Ви програли. Спробуйте ще раз!")
        print("-" * 20)

def play_guess_number():
    """Гра вгадай число"""
    number = random.randint(1, 20)
    attempts = 0
    print(f"\n{Fore.CYAN}--- ГРА: Вгадай число (від 1 до 20) ---")

    while True:
        choice = input("Введіть число або 'вихід': ")
        if choice.lower() == "вихід":
            break

        if not choice.isdigit():
            print(Fore.RED + "Будь ласка, введіть ціле число!")
            continue

        attempts += 1
        guess = int(choice)

        if guess < number:
            print(Fore.YELLOW +
                  f"Загадане число більше {emoji.emojize(':up_arrow:')} ")
        elif guess > number:
            print(Fore.YELLOW +
                  f"Загадане число менше! {emoji.emojize(':down_arrow:')} ")
        else:
            print(
                f"{Fore.GREEN}Вітаю! Ви вгадали число {number} за {attempts} спроб!")
            break        