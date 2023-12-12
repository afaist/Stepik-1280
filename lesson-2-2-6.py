"""
Загрузите цветное изображение из файла img.png. Подсчитайте яркость этого
изображения и сохраните в файл out_img.png. Результирующее изображение должно
быть одноканальным. Для подсчета яркости используйте формулу
Y=0.2126⋅R+0.7152⋅G+0.0722⋅B Y=0.2126⋅R+0.7152⋅G+0.0722⋅B , не забудьте сначала
перевести изображение в вещественные числа (функция img_as_float), а затем в
целые числа (функция img_as_ubyte).
"""
from skimage.io import imread, imsave
from skimage import img_as_ubyte, img_as_float

img = img_as_float(imread("img.png"))
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]
img_gray = img_as_ubyte(0.2126*r+0.7152*g+0.0722*b)
imsave("out_img.png", img_gray)
