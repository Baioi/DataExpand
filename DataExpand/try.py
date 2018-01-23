#coding:utf-8
#===================================================================================================
#文件说明:
#       第三节:图像处理---之---在python下,怎样使用OpenCv设置ROI区域
#开发环境：
#       Ubuntu14.04+Python2.7+IDLE+IPL
#时间地点:
#       陕西师范大学　2016.11.19
#作　　者:
#       九月
#===================================================================================================
'''''【模块１】感兴趣区域的设置ROI'''
#1--Python中ROI区域的设置也是使用Numpy中的索引来实现的
import cv2
import numpy as np
srcImg = cv2.imread('/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/nosign_1/0.jpg',cv2.CV_LOAD_IMAGE_COLOR) #[1]加载图片
cv2.namedWindow("[srcImg]",cv2.cv.CV_WINDOW_NORMAL)                    #[2]创建图片的显示窗口
cv2.moveWindow("[srcImg]",10,10)                                     #[3]让窗口在指定的位置显示
cv2.imshow("[srcImg]",srcImg)#[4]显示图片
Roi = cv2.imread('/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad-all1/p5.png',cv2.CV_LOAD_IMAGE_COLOR) #[1]加载图片
roiImg = Roi #[5]利用numpy中的数组切片设置ROI区域
h,w = Roi.shape[:2]
x=90
srcImg[x:x+w,x:x+h] = roiImg #[6]将设置的ROI区域添加到圆图像中
cv2.namedWindow("[ROIImg]",cv2.cv.CV_WINDOW_NORMAL)
cv2.moveWindow("[ROIImg]",600,100)
cv2.imshow("[ROIImg]",srcImg)
cv2.waitKey(0)
cv2.destroyWindow("[ROIImg]")                                          #[7]销毁窗口,Python编程中,最好加上这一句
cv2.destroyWindow("[srcImg]")