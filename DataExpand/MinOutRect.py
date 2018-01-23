#coding=utf-8
"""
寻找图像图像（圆形，三角，矩形）的最小外接矩形
"""
import cv2
def Min_out_rect(image_file):
    img = cv2.imread(image_file,-1)
    if img.shape[2] == 3:
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3)) 
        ret,img_binary = cv2.threshold(img_gray,160,255,cv2.THRESH_BINARY_INV)
        dilated = cv2.dilate(img_binary,kernel)
        _, contours,hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        # try:
        #     print contours[0]
        # except IndexError:
        #     cv2.imshow("img", img)
        #     cv2.imshow("bianry",img_binary)
        #     cv2.waitKey(0)
        x, y, w, h = cv2.boundingRect(contours[0])
        if w <= 10 or h <= 10:
            print '疑似尺寸错误' + image_file + '\n'
        cv2.drawContours(img,contours,-1,(0,0,255),3)##轮廓
        print len(contours)
        cv2.waitKey(0)
    else:
        r, g, b, a = cv2.split(img)
        rgb_img2 = cv2.merge((r, g, b))
        img_binary = a
        _, contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        x, y, w, h = cv2.boundingRect(contours[0])
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)  ##轮廓
    return x,y,w+x,h+y

def drawBBox(imgfile,x,y,x2,y2):
    # x,y,w,h = cv2.boundingRect(cnt)
    img = cv2.imread(imgfile, -1)
    cv2.rectangle(img,(x,y),(x2,y2),(0,255,0),2)
    cv2.imwrite('box.jpg',img)

if __name__ == "__main__":

    image_file =  r'D:\Workspaces\TrafficData\ExpandedSigns\B9\82.png'
    # drawBBox(cv2.imread(img),713,962,724,1080)
    x1,y1,x2,y2=Min_out_rect(image_file)
    drawBBox(image_file,x1,y1,x2,y2)
    print x1,y1,x2,y2


