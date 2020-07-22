# IMPORT THE NECESSARY LIBRARIES
from lane import Lane
import numpy as np
import cv2

def region_of_interest(img, vertices):
    """
    Defining an empty mask.
    It is a method that is necessary for the starting. Think of it as
    a blank canvas. Now, the necessary works will be done with the colors
    we want to that canvas, respectively.
    """
    mask = np.zeros(img)

    # Processing according to the number of channels in the mask.
    if len(img.shape) > 2:
    	channel_count = img.shape[2] # RGB or RGBA so 3 or 4
    	# 255 = white color.
    	# As I said above, all the remaining colors, except white, will be ignored.
    	ignore_mask_color = (255,) * channel_count
    else:
    	ignore_mask_color = 255

    # fillPoly: Fills the area bounded by one or more polygons.
    cv2.fillPoly(mask, vertices, ignore_mask_color)

	# returning the image only where mask pixels are nonzero.
	masked_image = cv2.bitwise_and(img, mask)

	return masked_image, mask



