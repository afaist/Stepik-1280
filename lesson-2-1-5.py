"""
Прочитайте изображение из файла img.png. У этого изображения нечетное
количество строк и столбцов. Поменяйте цвет центрального пикселя этого
изображения на зеленый цвет rgb (102, 204, 102) и сохраните изображение в файл
out_img.png.
"""
from skimage.io import imread, imsave

img = imread("img.png")
# Check size one pixel
if img[0, 0].size == 3:
    row = int((img.shape[0] - 1) / 2)
    col = int((img.shape[1] - 1) / 2)
    img[row, col] = [102, 204, 102]
    imsave("out_img.png", img)
