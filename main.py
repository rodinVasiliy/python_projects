# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

import numpy as np
from matplotlib import pyplot as plt
from skimage.exposure import histogram
from skimage.filters import median
from skimage.io import imread, imshow, show
from skimage.morphology import disk, diamond, star, rectangle
from skimage import data
from skimage.util import random_noise
from skimage.morphology import disk
from skimage.filters import median

settings = {'read_path': 'image.jpg',
            'save_path': 'new.jpg'
            }

# open file  and serialize settings in this file
with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

with open('settings.json') as info_data:
    json_data = json.load(info_data)

path = json_data['read_path']
image = imread(path)

# imshow(image)

# https://scikit-image.org/docs/stable/api/skimage.filters.html#skimage.filters.median
median_1 = median(image, np.dstack(rectangle(8, 6)), mode='wrap')
median_2 = median(image, np.dstack((diamond(5), diamond(5), diamond(5))), mode='nearest')
median_3 = median(image, np.dstack((disk(7), disk(7), disk(7))), mode='reflect')
median_4 = median(image, np.dstack((star(3), star(3), star(3))), mode='mirror')
median_5 = median(image, np.dstack((disk(7), disk(7), disk(7))), mode='mirror')

fig, axes=plt.subplots(nrows=2, ncols=3,figsize=( 15, 5))
axes[0][0].set_axis_off()
axes[0][0].imshow(image)
axes[0][1].set_axis_off()
axes[0][1].imshow(median_1)
axes[0][2].set_axis_off()
axes[0][2].imshow(median_2)
axes[1][0].set_axis_off()
axes[1][0].imshow(median_3)
axes[1][1].set_axis_off()
axes[1][1].imshow(median_4)
axes[1][2].set_axis_off()
axes[1][2].imshow(median_4)
show()

image_red = image[:, :, 2]
image_green = image[:, :, 1]
image_blue = image[:, :, 0]
hist_image_red, bins_red = histogram(image_red)
hist_image_green, bins_green = histogram(image_green)
hist_image_blue, bins_blue = histogram(image_blue)

median_1_red = median_1[:, :, 2]
median_1_green = median_1[:, :, 1]
median_1_blue = median_1[:, :, 0]
hist_median1_red, bins_median_red = histogram(median_1_red)
hist_median1_green, bins_median_green = histogram(median_1_green)
hist_median1_blue, bins_median_blue = histogram(median_1_blue)

fig1 = plt.figure(figsize=(10, 10))
fig1.add_subplot(2, 2, 1)
imshow(image)
fig1.add_subplot(2, 2, 2)
imshow(median_1)
fig1.add_subplot(2, 2, 3)
plt.plot(bins_red, hist_image_red, color='red')
plt.plot(bins_blue, hist_image_blue, color='blue')
plt.plot(bins_green, hist_image_green, color='green')
plt.legend(['red', 'blue', 'green'])
fig1.add_subplot(2, 2, 4)
plt.plot(bins_median_red, hist_median1_red, color='red')
plt.plot(bins_median_blue, hist_median1_blue, color='blue')
plt.plot(bins_median_green, hist_median1_green, color='green')
plt.legend(['red', 'blue', 'green'])
plt.tight_layout()
path_save = json_data['save_path']
plt.savefig(path_save)
show()

fig2 = plt.figure(figsize=(10, 10))
img = data.camera()
fig2.add_subplot(1, 3, 1)
imshow(img)
# salt and pepper
image1 = random_noise(img, mode="s&p")
fig2.add_subplot(1, 3, 2)
imshow(image1)
new = median(image1, diamond(5), mode='wrap')
fig2.add_subplot(1, 3, 3)
imshow(new)
show()



