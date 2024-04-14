import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_frame(i):
  """
  Функция для создания кадра ASCII-анимации шара.

  Args:
    i: Индекс кадра.

  Returns:
    Строка ASCII-арта, представляющая кадр анимации.
  """
  theta = i * np.pi / 180
  phi = np.pi / 2
  radius = 5

  x = radius * np.sin(phi) * np.cos(theta)
  y = radius * np.sin(phi) * np.sin(theta)
  z = radius * np.cos(phi)

  projection = np.array([x, y])
  min_val = np.min(projection, axis=0)
  max_val = np.max(projection, axis=0)

  normalized_projection = (projection - min_val) / (max_val - min_val)
  ascii_art = np.array([
      [" " if val < 0.25 else "#" if val < 0.75 else "*" for val in row]
      for row in normalized_projection
  ])

  return ascii_art.tostring().decode('utf-8')

num_frames = 360
frames = [create_frame(i) for i in range(num_frames)]

fig, ax = plt.subplots()
ax.imshow(np.zeros((10, 20)), cmap='Greys', aspect='auto')

animation = FuncAnimation(
    fig, lambda i: ax.set_data(np.fromstring(frames[i], dtype=np.uint8).reshape(10, 20)),
    frames=num_frames, interval=10, blit=True
)

plt.show()
