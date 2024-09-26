import cv2
import math

readimg = cv2.imread('image/fruit2.jpg')
maskSobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
maskSobelY = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]

# Convert the image to int32 to avoid overflow issues
readimg = readimg.astype('int32')

mOutImg = readimg.copy()
height, width, channel = readimg.shape

# Initialize arrays
pTmpXB = (width * height) * [0]
pTmpXG = (width * height) * [0]
pTmpXR = (width * height) * [0]
pTmpYB = (width * height) * [0]
pTmpYG = (width * height) * [0]
pTmpYR = (width * height) * [0]

mOutImg = mOutImg * 0

# Apply the Sobel mask
for i in range(1, height - 1):
    for j in range(1, width - 1):
        newValueBx = newValueGx = newValueRx = 0
        newValueBy = newValueGy = newValueRy = 0
        for mr in range(3):
            for mc in range(3):
                r, g, b = readimg[i + mc - 1, j + mr - 1]
                newValueBx += maskSobelX[mr][mc] * b
                newValueGx += maskSobelX[mr][mc] * g
                newValueRx += maskSobelX[mr][mc] * r
                newValueBy += maskSobelY[mr][mc] * b
                newValueGy += maskSobelY[mr][mc] * g
                newValueRy += maskSobelY[mr][mc] * r

        pTmpYB[i * width + j] = newValueBy
        pTmpYG[i * width + j] = newValueGy
        pTmpYR[i * width + j] = newValueRy
        pTmpXB[i * width + j] = newValueBx
        pTmpXG[i * width + j] = newValueGx
        pTmpXR[i * width + j] = newValueRx

# Convert negative values to positive
for i in range(1, height - 1):
    for j in range(1, width - 1):
        constBVal1, constGVal1, constRVal1 = pTmpXB[i * width + j], pTmpXG[i * width + j], pTmpXR[i * width + j]
        constBVal2, constGVal2, constRVal2 = pTmpYB[i * width + j], pTmpYG[i * width + j], pTmpYR[i * width + j]
        
        constBVal1 = abs(constBVal1)
        constGVal1 = abs(constGVal1)
        constRVal1 = abs(constRVal1)
        constBVal2 = abs(constBVal2)
        constGVal2 = abs(constGVal2)
        constRVal2 = abs(constRVal2)
        
        pTmpXB[i * width + j] = constBVal1 + constBVal2
        pTmpXG[i * width + j] = constGVal1 + constGVal2
        pTmpXR[i * width + j] = constRVal1 + constRVal2

# Normalize and find the magnitude
for i in range(1, height - 1):
    for j in range(1, width - 1):
        magnitude = math.sqrt(pTmpXB[i * width + j] ** 2 + pTmpYB[i * width + j] ** 2 +
                              pTmpXG[i * width + j] ** 2 + pTmpYG[i * width + j] ** 2 +
                              pTmpXR[i * width + j] ** 2 + pTmpYR[i * width + j] ** 2)

        # Apply thresholding to extract edges
        threshold = 180
        if magnitude < threshold:
            mOutImg[i, j] = [255, 255, 255]  # White for edges
        else:
            mOutImg[i, j] = [0, 0, 0]  # Black for non-edges

# Convert back to uint8 to display
mOutImg = mOutImg.astype('uint8')

cv2.imshow("Sobel Edge Detection", mOutImg)
cv2.imshow("Origin", readimg.astype('uint8'))  # Convert original image back to uint8 for display
cv2.waitKey()
