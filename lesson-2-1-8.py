"""
Загрузите изображение из файла img.png. Изображение состоит из рамки сплошного
цвета и внутренней части изображения. Цвет рамки можно узнать, посмотрев на
левый верхний пиксель. Рамка может иметь разную ширину со всех четырех сторон.
Определите размеры рамки и выведите эти размеры через пробел. Размеры рамки
выводите в следующем порядке: левый, верхний, правый, нижний.
"""
from skimage.io import imread
import numpy as np

img = imread("img.png")

height, width = img.shape[:2]
# left border
LEFT = 1
RIGHT = 0
UPPER = 1
BOTTOM = 0
left_border = img[0:height, 0]
upper_border = img[0, 0:width]
for i in range(1, width // 2):
    if np.array_equal(left_border, img[0:height, i]):
        LEFT += 1
    else:
        break
for i in range(width - 1, width // 2, -1):
    if np.array_equal(left_border, img[0:height, i]):
        RIGHT += 1
    else:
        break
for i in range(1, height // 2):
    if np.array_equal(upper_border, img[i, 0:width]):
        UPPER += 1
    else:
        break
for i in range(height - 1, height // 2, -1):
    if np.array_equal(upper_border, img[i, 0:width]):
        BOTTOM += 1
    else:
        break
print(LEFT, UPPER, RIGHT, BOTTOM)
