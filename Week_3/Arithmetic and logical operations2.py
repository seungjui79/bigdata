import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('images/img3.jpg')
img2 = cv.imread('images/img4.jpg')

#cv.subtract(   src1, src2[,    dst[, mask[, dtype]]]   ) ->    dst
img3 = cv.subtract(img1, img2)

# cv.absdiff(   src1, src2[, dst]   ) ->    dst
img4 = cv.asdiff(img1, img2)

titles = ['src', 'map', 'sub', 'absDiff']
imgs = [img1, img2, img3, img4]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()