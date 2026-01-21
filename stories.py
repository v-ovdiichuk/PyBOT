import emoji
import random
from colorama import Fore, Style, init
from time import sleep
from tqdm import tqdm


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
