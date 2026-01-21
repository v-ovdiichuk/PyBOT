from colorama import Fore, Style, init
from time import sleep
from tqdm import tqdm
from prettytable import PrettyTable


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
