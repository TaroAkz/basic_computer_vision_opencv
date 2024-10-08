from math import floor
import cv2
img = cv2.imread('image/glass.jpg')
copy_img = img.copy()
height,width,kernel = copy_img.shape

histoB=(256)*[0]
histoG=(256)*[0]
histoR=(256)*[0]
LUTB=(256)*[0]
LUTG=(256)*[0]
LUTR=(256)*[0]

for i in range(height):
    for j in range(width):
        r,g,b = img[i,j]
        histoR[r]+=1
        histoG[g]+=1
        histoB[b]+=1
#build histogram original
for i in range(256):
    #change if i ==0 so we give histogram equal to its index at 0
    
    if i == 0:
        histoB[i]=histoB[0]
        histoG[i]=histoG[0]
        histoR[i]=histoR[0]
    else:
        #check the rest calculate like take current index + index-1
        histoB[i]=histoB[i]+histoB[i-1]
        histoG[i]=histoG[i]+histoG[i-1]
        histoR[i]=histoR[i]+histoR[i-1]
#transform histogram
for i in range(256):
    LUTB[i] = (float(histoB[i])/float(width*height))*255
    LUTG[i] = (float(histoG[i])/float(width*height))*255
    LUTR[i] = (float(histoR[i])/float(width*height))*255
for i in range(height):
    for j in range(width):
        # Write your code here
        r, g, b = img[i, j]
        new_r = LUTR[r]
        new_g = LUTG[g]
        new_b = LUTB[b]
        copy_img[i, j] = [new_b, new_g, new_r]

cv2.imshow('Histogram',copy_img)
cv2.imshow("Original",img)
cv2.waitKey()