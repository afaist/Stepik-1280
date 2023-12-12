import skimage.color as sc
from skimage import data
import numpy as np
import matplotlib.pyplot as plt

# astronaut
img = data.astronaut()
img_gray = sc.rgb2gray(data.astronaut())

img_converted = sc.convert_colorspace(img, "RGB", "HSV")
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')
ax1.imshow(img)
ax2.imshow(img_converted)
plt.show()
