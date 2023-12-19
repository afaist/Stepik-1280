from skimage.io import imread, imsave

img = imread("img.png")
x_min = img.min()
x_max = img.max()
img = img - x_min
diff = 255 / (x_max - x_min)
img = img * diff
img = img.astype("uint8")
imsave("out_img.png", img)
a = 3 * 5
