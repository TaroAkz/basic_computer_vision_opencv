import cv2 as cv

img = cv.imread('image/glass.jpg')

modified_val = 30
def darkness(img, modified_value):
    dark_img = img.copy()
    height, width, _ =img.shape
    for i in range(height):
        for j in range(width):
            # Access the pixel intensities
            pixel_org = img[i, j]
            pixel_dark = dark_img[i, j]
            
            pixel_dark[0] = max(0, pixel_org[0] - modified_value)
            pixel_dark[1] = max(0, pixel_org[1] - modified_value)
            pixel_dark[2] = max(0, pixel_org[2] - modified_value)
    return dark_img

def brightness(img, modified_value):
    bright_img = img.copy()
    height, width, _ =img.shape
    for i in range(height):
        for j in range(width):
            # Access the pixel intensities
            pixel_org = img[i, j]
            pixel_dark = dark_img[i, j]
            
            bright_img[0] = max(255, pixel_org[0] + modified_value)
            bright_img[1] = max(255, pixel_org[1] + modified_value)
            bright_img[2] = max(255, pixel_org[2] + modified_value)
    return bright_img
            
dark_img = darkness(img, modified_val)
bright_img = brightness(img, modified_val)

cv.imshow("Original",img)
cv.imshow("Brightness",dark_img)
cv.imshow("Darkness",bright_img)
cv.waitKey()