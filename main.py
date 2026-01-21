from art import tprint
from colorama import Fore, Style, init
import emoji
import games
from jokes import get_joke
from recomendations import show_recomendations
from storys import get_intresting_story

# Ініціалізація колорама для кольорового тексту

init(autoreset=True)


def show_welcome():
    """Виводить привітання при запуску!"""
    tprint("PyBOT V1.0", font="bulbhead")
    print(Fore.CYAN + "Вітаю у розважальному боті!")
    print("-----------------------------------------")


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
        print(
            f"2. Розсміши мене {emoji.emojize(':rolling_on_the_floor_laughing:')}")
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
