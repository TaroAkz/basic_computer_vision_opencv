import cv2 as cv
img = cv.imread("image/fruit1.jpg")

#dimension
height, width, channel = img.shape


print('Height: ', height)
print('Width: ', width)
print('Channel: ', channel)

for i in range(height):
    for j in range(width):
        # B, G, R = cv.split(img)
        B, G, R = img[i, j]
        gray_value = int(0.299 * R + 0.587 * G + 0.114 * B)
        img[i, j,0] = gray_value
        img[i, j,1] = gray_value
        img[i, j,2] = gray_value
        #img[i, j] = [gray_value, gray_value, gray_value]


cv.imwrite('image/greyfruit.jpg', img)
cv.imshow('img',img)
cv.waitKey(10000)