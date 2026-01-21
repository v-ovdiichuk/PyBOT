import random
from art import tprint
from colorama import Fore, Style, init
import pyjokes
from time import sleep
from tqdm import tqdm
from prettytable import PrettyTable
import emoji
import games

# Ініціалізація колорама для кольорового тексту

init(autoreset=True)


def show_welcome():
    """Виводить привітання при запуску!"""
    tprint("PyBOT V1.0", font="bulbhead")
    print(Fore.CYAN + "Вітаю у розважальному боті!")
    print("-----------------------------------------")


def get_joke():
    """Функція для виводу анекдоту"""
    print(Fore.YELLOW + "Хвилинку згадую щось смішне...")
    # Імітація завантаження
    for _ in tqdm(range(10), desc="Завантаження"):
        sleep(0.05)
    joke = pyjokes.get_joke()
    print(f"\n{Fore.GREEN}Анекдот: {Style.BRIGHT}{joke}\n")


def show_recomendations():
    """Меню рекомендацій контенту"""
    while True:
        print(f"\n{Fore.MAGENTA}Що саме вас цікавить?")
        print("1. Фільми")
        print("2. Відеоігри")
        print("3. Назад")

        choice = input(f"{Fore.WHITE}Оберіть категорію: ")

        if choice == "1":
            content = {
                "Фантастика": ["Інтерстеллер", "Початок", "Матриця"],
                "Комедія": ["Завжди кажи 'ТАК'", "Один вдома", "Маска"],
                "Драма": ["Зелена миля", "Форест Гамп", "Список Шиндлера"]
            }
            display_table("Фільми", content)
        elif choice == "2":
            content = {
                "RPG": ["The Witcher 3", "Skyrim", "Elden Ring"],
                "Shooter": ["Doom Eternal", "CS 2", "HALF-LIFE 2"],
                "Strategy": ["Civilization VI", "StarCraft II", "Anno 1800"]
            }
            display_table("Відеоігри", content)
        elif choice == "3":
            print(Fore.YELLOW + "Повертаємось...")
            break
        else:
            print(Fore.RED + "Невірний вибір, спробуйте ще раз.")


def display_table(category_name, data):
    """Створює та виводить таблицю з даними"""
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}Жанр", f"{Fore.CYAN}Рекомендації"]
    # Додаємо рядки в таблицю
    for genre, items in data.items():
        # Обєднуємо список у рядки через кому
        table.add_row([genre, ", ".join(items)])
     # Імітація завантаження
    for _ in tqdm(range(10), desc="Завантаження"):
        sleep(0.05)
    print(f"\n{Fore.YELLOW}ТОП-рекомендації для категорії {category_name}")
    print(table)
    print("\n")




def get_intresting_story():
    """Виводить випадкову цікаву історію або факт"""
    stories = [
        f"{emoji.emojize(':elephant:')} Слон - єдина тварина, яка не вміє стрибати. Але вони чудові плавці!",
        f"{emoji.emojize(':honey_bee:')} Мед ніколи не псується. Археологи знаходили мед у давньоєгипетських гробницях, якому понад 3000 років, і він досі їстівний!",
        f"{emoji.emojize(':octopus:')} У восьминога три серця, а його кров синього кольору.",
        f"{emoji.emojize(':sparkles:')} Алмази можна виготовити з арахісового масла (під дуже високим тиском, звісно).",
        f"{emoji.emojize(':cat_face:')} Коти сплять близько 70% свого життя."
    ]
    print(f"\n{Fore.CYAN}--- ХВИЛИНКА ЦІКАВОГО ---")
    # Ефект завантаження з емодзі
    for _ in tqdm(range(5), desc=emoji.emojize("Шукаю факти :magnifying_glass_tilted_left:")):
        sleep(0.2)

    story = random.choice(stories)
    print(f"\n{story}\n")


def game_menu():
    """Меню вибору ігор"""
    while True:
        print(f"\n{Fore.GREEN}--- Оберіть гру ---")
        print("1. Камінь, ножиці, папір")
        print("2. Вгадай число")
        print("3. Назад до головного меню")

        choice = input(f"{Fore.WHITE}Ваш вибір: ")

        if choice == "1":
            games.play_rps()
        elif choice == "2":
            games.play_guess_number()
        elif choice == "3":
            print(Fore.YELLOW + "Повертаємось...")
            print("\n")
            break
        else:
            print(Fore.RED + "Невірний вибір!")


def main_menu():
    """Головне меню програми"""
    while True:
        print(f"{Fore.BLUE}--- ГОЛОВНЕ МЕНЮ {emoji.emojize(':robot:')} ---")
        print(f"1. Рекомендації {emoji.emojize(':clapper_board:')}")
        print(f"2. Розсміши мене {emoji.emojize(':rolling_on_the_floor_laughing:')}")
        print(f"3. Пограти в гру {emoji.emojize(':video_game:')}")
        print(f"4. Цікава історія {emoji.emojize(':light_bulb:')}")
        print(f"0. Вихід {emoji.emojize(':door:')}")

        choice = input(f"{Fore.WHITE}Оберіть пункт: ")

        if choice == '1':
            show_recomendations()
        elif choice == '2':
            get_joke()
        elif choice == '3':
            game_menu()
        elif choice == '4':
            get_intresting_story()
        elif choice == '0':
            print(Fore.RED + emoji.emojize("Бувай! Повертайся ще :wave:"))
            break
        else:
            print(Fore.RED + "Помилка! Оберіть пункт від 0 до 4.")


if __name__ == "__main__":
    show_welcome()
    main_menu()