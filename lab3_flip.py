import cv2 as cv

img = cv.imread('image/facetree.jpg')

x, y , _ = img.shape
img1 = img.copy()

for i in range(0, x):
    for j in range(0, y):
        img1[i][j] = img[i][y-j-1]
        
cv.imwrite('grey_image.jpg', img1)    

cv.imshow('Original',img)
cv.imshow('flip_img',img1)
cv.waitKey(10000)