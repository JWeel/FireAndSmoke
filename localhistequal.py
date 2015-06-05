# Standard imports
import cv2
import numpy as np;
from matplotlib import pyplot as plt

#img = cv2.imread("sl11.jpg", cv2.IMREAD_COLOR)


# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(32,32))
cl1 = clahe.apply(hsv[2])

# Create histogram
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# Create histogram graph
plt.hist(cl1.ravel(),256,[0,256]); plt.show()

# Attach input and output images horizontally
res = np.hstack((img,hsv))

# Show output image
cv2.imshow("Equalized image", res)
cv2.waitKey(0)
