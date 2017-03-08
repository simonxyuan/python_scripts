import sys
from PIL import Image
import cv2
import Tkinter as tk

crop_width = 64

testFile = 'test.png'
img = cv2.imread(testFile)


root = tk.Tk()
w = tk.Canvas(root, width = 800, height = 600, bd = 10, bg = 'white')
w.grid(row 



        
print img.shape
(imgHeight, imgWidth, channels) = img.shape

rangefor x in range(0, imgHeight - 0.75 * crop_width, crop_width/4):
    for y in range(0, imgWidth - 0.75 * crop_width, crop_width/4):
        patch = img[x : x + crop_width, y : y + crop_width]
        tempImg = img.copy()
        cv2.rectangle(tempImg, (y, x), (y + crop_width, x + crop_width), (255, 0, 0), 5)
        #cv2.rectangle(tempImg, (100,100), (500,500), (255,0,0), 5)
        tempImg = cv2.resize(tempImg,  None, fx = 0.3, fy = 0.3)
        cv2.imshow('image', tempImg)
        cv2.imshow('Patch', patch)
        cv2.waitKey(0)

            

