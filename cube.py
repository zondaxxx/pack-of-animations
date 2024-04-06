import time
from math import pi, sin, cos

# Размеры куба
WIDTH = 10
HEIGHT = 10
DEPTH = 10

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

# Функция для отображения куба
def draw_cube(angle_x, angle_y, angle_z):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Вычисление координат точки на поверхности куба
            x = (i - HEIGHT // 2) * cos(angle_y) * sin(angle_z) - (j - WIDTH // 2) * sin(angle_y) * cos(angle_z)
            y = (i - HEIGHT // 2) * sin(angle_y) * cos(angle_z) + (j - WIDTH // 2) * cos(angle_y) * sin(angle_z)
            z = (i - HEIGHT // 2) * cos(angle_x)

            # Вычисление расстояния до центра
            distance = ((x ** 2 + y ** 2 + z ** 2) ** 0.5) ** 0.5

            # Выбор символа и цвета
            if distance <= DEPTH // 2:
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
angle_x = 0
angle_y = 0
angle_z = 0
while True:
    draw_cube(angle_x, angle_y, angle_z)
    angle_x += 0.01
    angle_y += 0.02
    angle_z += 0.03
    time.sleep(0.1)
