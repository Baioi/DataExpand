#coding=utf-8
"""
该函数的作用是把交通标志粘贴到no-sign的街景图像中，
交通标志叠加，边缘的白色部分融合在街景图中
"""
import cv2
import numpy as np
def Images_fusion(image_file1,image_file2,x,y,outputfile):
    """
    用轮廓做mask实现交通标志和街景图的融合
    :param image_file1: 街景图
    :param image_file2: 交通标志图
    :param x:
    :param y:
    :return:
    """
    img1 = cv2.imread(image_file1)
    img2 = cv2.imread(image_file2, -1)
        # cv2.namedWindow("Before", cv2.cv.CV_WINDOW_NORMAL)  # [2]创建图片的显示窗口
        # cv2.moveWindow("Before", 10, 10)
        # cv2.imshow("Before", img1)  # [4]显示图片
    h, w = img2.shape[:2]
    x = int(x)
    y = int(y)
    roi = img1[y:y+h, x:x+w]
    # print x, y
    # print roi.shape
    if img2.shape[2] == 3:
        img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('img2gray',img2gray)
        ret,binary = cv2.threshold(img2gray,160,255,cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5)) 
        dilated = cv2.dilate(binary,kernel)
        binary = cv2.bitwise_not(dilated)
        _, contours, _ = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(img2, contours, -1, (0, 0, 255), 2)
        mask = np.zeros(img2.shape).astype(img2.dtype)
        color = [255, 255, 255]
        cv2.fillPoly(mask, contours, color)
        mask_ori = cv2.bitwise_and(img2, mask)
        # cv2.imwrite("./mask_ori.jpg", mask_ori)
        # cv2.imwrite("./mask.jpg", mask)
        mask = cv2.bitwise_not(mask)
        roi = cv2.bitwise_and(mask, roi)
        roi = cv2.bitwise_or(mask_ori, roi)
        # cv2.imwrite("./roi.jpg", roi)
        img1[y:y+h, x:x+w] = roi
        cv2.imwrite(outputfile, img1)
        # cv2.waitKey(0)
        # cv2.imshow('result',img1)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        r, g, b, a = cv2.split(img2)
        rgb_img2 = cv2.merge((r, g, b))
        mask_inv = cv2.bitwise_not(a)
        # cv2.imwrite("rgb_alpha_inv.jpg", mask_inv)
        mask_inv = cv2.merge((mask_inv, mask_inv, mask_inv))
        mask = cv2.merge((a, a, a))
        rgb_img2_clear = cv2.bitwise_and(mask, rgb_img2)
        cv2.imwrite("rgb_img2_clear.jpg", rgb_img2_clear)
        # print mask_inv.shape
        roi = cv2.bitwise_and(mask_inv, roi)
        roi = cv2.bitwise_or(rgb_img2_clear, roi)
        # cv2.imwrite("roi.jpg", roi)
        img1[y:y+h, x:x+w] = roi
        cv2.imwrite(outputfile, img1)

def images_fusion(image_file1,image_file2,x,y,outputfile):
    """
    :param image_file1: 街景图
    :param image_file2: 交通标志图
    :param x:
    :param y:
    :return:
    """
    img1 = cv2.imread(image_file1, cv2.CV_LOAD_IMAGE_COLOR)
    img2 = cv2.imread(image_file2, cv2.CV_LOAD_IMAGE_COLOR)
    # cv2.namedWindow("Before", cv2.cv.CV_WINDOW_NORMAL)  # [2]创建图片的显示窗口
    # cv2.moveWindow("Before", 10, 10)
    # cv2.imshow("Before", img1)  # [4]显示图片
    w,h = img2.shape[:2]

    roi = img1[x:w+x,y:y+h]

    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('img2gray',img2gray)
    ret,mask = cv2.threshold(img2gray,165,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    #cv2.imshow('mask',mask)
    cv2.waitKey(0)
    #cv2.imshow('make_inv',mask_inv)
    cv2.waitKey(0)

    img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
    roi2 = img1_bg[75:205,75:205] ##保持交通标志里面的颜色依然是白色
    _,img1_bg_true = cv2.threshold(roi2,80,255,cv2.THRESH_BINARY)
    img1_bg[75:205,75:205]=img1_bg_true
    #cv2.imshow('bg',img1_bg)
    img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)
    #cv2.imshow('fg',img2_fg)
    dst = cv2.add(img1_bg,img2_fg)
    img1[x:x+w,y:y+h]=dst
    cv2.imwrite(outputfile,img1)

    # cv2.waitKey(0)
    # cv2.imshow('result',img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    image_file1='24.jpg'
    image_file2='10.png'

    out_file='./out.jpg'

    #ROI_image_fusion(image_file1,image_file2,100,100)
    Images_fusion(image_file1,image_file2,400,100, out_file)









