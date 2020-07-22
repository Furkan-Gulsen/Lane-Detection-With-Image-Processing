import numpy as np
import matplotlib.pyplot as plt
import cv2

woman = cv2.imread("woman.jpeg")
image = cv2.imread("image.jpeg")

cv2.imshow("woman", woman)
cv2.imshow("image", image)

# weightedSum = cv2.addWeighted(woman, 0.5, image, 0.4, 0)
# cv2.imshow("weightedSum", weightedSum)

# subtract = cv2.subtract(woman, image)
# cv2.imshow("subtract", subtract)

# CREATE MASK
mask = np.zeros_like(image)

# AND
bitwise_and = cv2.bitwise_and(woman, image)
cv2.imshow("bitwise_and", bitwise_and)

# OR
bitwise_or = cv2.bitwise_or(woman, image)
cv2.imshow("bitwise_or", bitwise_or)

# XOR
bitwise_xor = cv2.bitwise_xor(woman, image)
cv2.imshow("bitwise_xor", bitwise_xor)

# NOT
bitwise_not = cv2.bitwise_not(woman, image)
cv2.imshow("bitwise_not", bitwise_not)

if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()