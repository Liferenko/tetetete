import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
# this block just show me img in gray colour
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# this one add graphic for img and some simple manipulation tools
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# #
# plt.plot([50,100],[80,100], 'b', linewidth=1)
# plt.show()

# this save new file with photo
cv2.imwrite('watchgray.png', img)