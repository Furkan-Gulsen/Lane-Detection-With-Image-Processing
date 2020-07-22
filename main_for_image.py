# IMPORT THE NECESSARY LIBRARIES
import os
import cv2
from collections import deque
import matplotlib.pyplot as plt
from os.path import join, basename
from lane_detection import color_frame_pipeline



resize_h, resize_w = 540, 960

# test on images
test_images_dir = join('data','test_images')
test_images = [join(test_images_dir, name) for name in os.listdir(test_images_dir)]

for test_img in test_images:
	print("Processing image: {}".format(test_img))

	out_path = join("out","images",basename)
    in_image = cv2.cvtColor(cv2.imread(test_img, cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
    out_image = color_frame_pipeline([in_image], solid_lines=True)
    cv2.imwrite(out_path, cv2.cvtColor(out_image, cv2.COLOR_RGB2BGR))
    plt.imshow(out_image)
    plt.waitforbuttonpress()

plt.close('all')