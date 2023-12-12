"""
﻿Загрузите изображение из файла img.png. У этого изображения поменяйте
местами каналы так, чтобы вместо порядка RGB каналы шли в порядке BRG.
Сохраните изображение с измененными каналами в файл out_img.png.
"""
from skimage.io import imread, imsave
import numpy as np

img = imread("img.png")
r, g, b = np.dsplit(img, 3)

img = np.dstack((b, r, g))
imsave("out_img.png", img)

# Or
# imsave("out_img.png", imread("img.png")[:, :, [2, 0, 1]])
