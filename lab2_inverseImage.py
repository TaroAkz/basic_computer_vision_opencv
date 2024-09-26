import cv2 as cv

img = cv.imread('image/fruit1.jpg')

height, width , _ = img.shape

for i in range(0, height):
    for j in range(0, width):
        B = img[i,j,0]
        G = img[i,j,1]
        R = img[i,j,2]
        
        
        img[i,j,[0]] = [abs(255-B)]
        img[i,j,[1]] = [abs(255-G)]
        img[i,j,[2]] = [abs(255-R)]
        
        # img[i,j,1] = grey_color
        # img[i,j,2] = grey_color
cv.imwrite('image/inverted_image.jpg', img)    
cv.imshow('Test Image',img)
cv.waitKey(10000)