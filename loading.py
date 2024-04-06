import random
import time

# Символы для анимации
CHARS = ["⢿", "⣻", "⢿", "⣻", "⢿", "⣻", "⢿", "⣻", "⢿", "⣻"]

# Цвета для анимации
COLORS = [
    (255, 0, 0),
    (255, 128, 0),
    (255, 255, 0),
    (128, 255, 0),
    (0, 255, 0),
    (0, 255, 128),
    (0, 255, 255),
    (0, 128, 255),
    (0, 0, 255),
    (128, 0, 255),
]

# Ширина анимации
WIDTH = 80

# Функция для отображения анимации
def draw_animation():
    for i in range(WIDTH):
        # Выбор случайного символа и цвета
        char = random.choice(CHARS)
        color = random.choice(COLORS)

        # Отображение символа
        print(f"\033[{i + 1};{1}H\033[38;2;{color[0]};{color[1]};{color[2]}m{char}", end="")

    # Очистка строки
    print("\033[K", end="")

# Запуск анимации
while True:
    draw_animation()
    time.sleep(0.1)
