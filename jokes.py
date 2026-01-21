from colorama import Fore, Style, init
from time import sleep
from tqdm import tqdm
import pyjokes


def get_joke():
    """Функція для виводу анекдоту"""
    print(Fore.YELLOW + "Хвилинку згадую щось смішне...")
    # Імітація завантаження
    for _ in tqdm(range(10), desc="Завантаження"):
        sleep(0.05)
    joke = pyjokes.get_joke()
    print(f"\n{Fore.GREEN}Анекдот: {Style.BRIGHT}{joke}\n")
