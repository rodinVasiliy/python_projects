# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
from matplotlib import pyplot as plt
from skimage.io import imread, imsave, imshow, show
from skimage.filters import median
from skimage.morphology import disk, diamond, star, rectangle
import numpy as np

settings = {'parameter_0': 'image.jpg'
            }

# open file  and serialize settings in this file
with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

with open('settings.json') as info_data:
    json_data = json.load(info_data)

path = json_data['parameter_0']
image = imread(path)
print(image.shape)
imshow(image)

median_1 = median(image, np.dstack(rectangle(8,6)), mode='wrap')
median_2 = median(image, np.dstack((diamond(5),diamond(5),diamond(5))), mode='nearest')
median_3 = median(image, np.dstack((disk(7),disk(7),disk(7))), mode='reflect')
median_4 = median(image, np.dstack((star(3),star(3),star(3))), mode='mirror')
median_5 = median(image, np.dstack((disk(7),disk(7),disk(7))), mode='mirror')

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