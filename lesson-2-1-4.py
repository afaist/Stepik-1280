"""
Прочитайте изображение из файла img.png и выведите количество столбцов этого
изображения на стандартный вывод.
"""
from skimage.io import imread

img = imread("img.png")
print(img.shape[1])
