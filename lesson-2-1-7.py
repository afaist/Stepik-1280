"""
Загрузите изображение из файла img.png. Оно имеет нечетное количество строк и
столбцов. В центре этого изображения находится прямоугольник размером 7 строк и
15 столбцов. Поменяйте его цвет на розовый rgb(255, 192, 203) и сохраните в
файл out_img.png.
"""
from skimage.io import imread, imsave

img = imread("img.png")
height, width = img.shape[:2]
top = (height - 7) // 2
left = (width - 15) // 2
img[top : top + 7, left : left + 15] = [255, 192, 203]

imsave("out_img.png", img)
