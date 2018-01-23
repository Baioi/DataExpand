#coding=utf-8
import numpy as np
import cv2
import os
import random
from Resize import deformation
from Resize import resize
from Rotate import Rotate
from LightChang import ChangeLightPower
import random
from ImagesFusion import images_fusion
from MinOutRect import Min_out_rect
"""
图像的随机（在一定范围内）旋转，缩放，光照强度变化
"""
##图像中心
def findCenter(img):
    (h,w)=img.shape[:2]
    center = (w/2,h/2)
    return center

if __name__ == "__main__":
    images_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/NEW1'
    file_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad-all1'
    out_path1 =  '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad1'
    out_path2 = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/NEW1'
    """以下用于生成更多的交通标志，变大变小，旋转光照也做一些变化等"""
    # image_name = os.listdir(file_path)
    # for images in image_name:
    #     img_name, ext = images.split('.')
    #     img_path = os.path.join(file_path,images)
    #     img = cv2.imread(img_path)
    #     # win1 = cv2.namedWindow('Original', flags=0)
    #     # cv2.imshow("Original",img)
    #     image_file_path = os.path.join(out_path,img_name)
    #     isExists = os.path.exists(image_file_path)
    #     if not isExists:
    #         os.makedirs(image_file_path)
    #         print image_file_path+'创建成功！'
    #     else:
    #         print image_file_path+'目录已存在！'
    #
    #     for i in range(0,1600):
    #         x = random.randint(-15,15)
    #         y = random.randint(50,460)
    #         a = random.uniform(0.68,1.2)
    #         image = Rotate(img,x)
    #         image = resize(image,width=y,height=None)
    #         image = deformation(image,a)
    #         # light_a = random.normalvariate(0.88,1.2)
    #         # light_b = random.uniform(-10,10)
    #         # image = ChangeLightPower(image,light_a,light_b)
    #         # h, w = image.shape[:2]
    #         # image = image[int(w*0.12):int(w*0.95),int(h*0.1):int(h*0.93)]
    #         cv2.imwrite(image_file_path+'/'+str(i)+'.jpg',image)

    """以下用以将交通标志图标和街景图融合在一起，写出XML"""
    Traffic_signs = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad1'
    Street_views = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/NEW1'
    output_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/创造的图像数据'
    out_xml_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/创造的图像数据/XML'
    Traffic_sign_files = os.listdir(Traffic_signs)
    Street_vies_image = os.listdir(Street_views)
    for images_file in Traffic_sign_files:
        images = os.listdir(images_file)
        for traffic_sign in images:
            street_img = random.sample(Street_vies_image,1)[0]
            street_img_path = os.path.join(Street_views,street_img)
            traffic_sign_path = os.path.join(Traffic_signs,images_file,traffic_sign)
            x1,y1,x2,y2=Min_out_rect(traffic_sign_path)
            a = random.uniform(350, 1700)
            b = random.uniform(300,1300)
            images_fusion(street_img_path,traffic_sign_path,a,b,outputfile=os.path.join(output_path,street_img)) ##注意不同的图像这里要用不用的
            a1=x1+a
            a2=x2+a
            b1=y1+b
            b2=y2+b

            """写入XML的程序"""
            attrs = dict()
            attrs['name'] = street_img
            attrs['classification'] = _CLASS
            attrs['xmin'] = str(a1)
            attrs['ymin'] = str(b1)
            attrs['xmax'] = str(a2)
            attrs['ymax'] = str(b1)











    #     if cv2.waitKey(0) & 0xFF == ord('q'):
    #         break
    # cv2.destroyAllWindows()








