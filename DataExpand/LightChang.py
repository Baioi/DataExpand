#coding=utf-8
import cv2
##改变图像的光照
def ChangeLightPower(RGBimg,a,b):
    rows, cols, channels = RGBimg.shape
    dst = RGBimg.copy()
    for i in range(rows):
        for j in range(cols):
            for c in range(3):
                color = RGBimg[i, j][c] * a + b
                if color > 255:
                    dst[i, j][c] = 255
                elif color < 0:
                    dst[i, j][c] = 0
    return dst

from skimage import io, data, exposure, img_as_float
##改变图像的光照
def ChangeLightPower(image, factor):
    gam1= exposure.adjust_gamma(image, factor)   #调暗
    return gam1

