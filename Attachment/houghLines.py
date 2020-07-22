import cv2
import numpy as np

img = cv2.imread('sudoku.png', cv2.IMREAD_COLOR) # road.png is the filename
# Convert the image to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)
cv2.imshow("edges",edges)

# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250)
# Draw lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# Show result

img = cv2.resize(img, dsize=(600, 600))
cv2.imshow("Result Image", img)

if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()