"""
Прочитайте изображение из файла img.png. У этого изображения нечетное
количество строк и столбцов. Вычислите негатив изображения и сохраните его в
файл out_img.png.
"""
from skimage.io import imread, imsave

img = imread("img.png")
new_image = 255-img
imsave("out_img.png", new_image)

