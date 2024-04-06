import time

# Символы для анимации
CHARS = [" ", ".", "*", "o", "O", "@", "#", "$", "%", "^", "&", "*"]

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

# Ширина и высота сердечка
WIDTH = 20
HEIGHT = 10

# Функция для отображения сердечка
def draw_heart():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Вычисление расстояния до центра
            distance = ((i - HEIGHT // 2) ** 2 + (j - WIDTH // 2) ** 2) ** 0.5

            # Выбор символа и цвета
            if distance <= WIDTH // 2:
                char = random.choice(CHARS)
                color = random.choice(COLORS)
            else:
                char = " "
                color = (0, 0, 0)

            # Отображение символа
            print(f"\033[{i + 1};{j + 1}H\033[38;2;{color[0]};{color[1]};{color[2]}m{char}", end="")

    # Очистка строки
    print("\033[K", end="")

# Запуск анимации
while True:
    draw_heart()
    time.sleep(0.1)
