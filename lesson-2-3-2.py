"""
Напишите функцию align, которая сопоставляет изображения с фотографий
Прокудина-Горского и возвращает координаты точек на синем и красном каналах,
как это описано в видео, слайдах и описании задания.
"""
from numpy import roll
from skimage import img_as_float
from skimage.io import imread


def align(img, coord):
    img = img_as_float(img)
    height = img.shape[0] // 3
    # Slides
    blue = img[:height, :]
    green = img[height:height * 2, :]
    red = img[height * 2:height * 3, :]
    # Border
    border_width = int(img.shape[1] * 0.15)
    border_height = int(height * 0.15)
    # Cut
    blue = blue[border_height:-1 - border_height, border_width:-1 - border_width]
    green = green[border_height:-1 - border_height, border_width:-1 - border_width]
    red = red[border_height:-1 - border_height, border_width:-1 - border_width]

    best_blue_correlation = -1
    best_red_correlation = -1
    bdy = bdx = rdy = rdx = 0
    for dy in range(-15, 16):
        for dx in range(-15, 16):
            db = roll(blue, dy, axis=0)
            db = roll(db, dx, axis=1)
            green_correlation = (db * green).sum()
            if green_correlation > best_blue_correlation:
                best_blue_correlation = green_correlation
                bdy = dy
                bdx = dx
            dr = roll(red, dy, axis=0)
            dr = roll(dr, dx, axis=1)
            red_correlation = (dr * green).sum()
            if red_correlation > best_red_correlation:
                best_red_correlation = red_correlation
                rdy = dy
                rdx = dx
    y, x = coord
    return (y - height - bdy, x - bdx), (y + height - rdy, x - rdx)


img = imread("img.png")
print(align(img, (508, 237)))
