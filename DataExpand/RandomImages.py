# -*- coding:utf-8 -*-
import numpy as np
import random
import cv2
import os
file_path='/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/nosign_1'
out_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/new'
image_name = os.listdir(file_path)
catch_images = random.sample(image_name,2000)
i =0
for images in catch_images:
    i=i+1
    img_path = os.path.join(file_path,images)
    img = cv2.imread(img_path)
    cv2.imwrite(out_path+'/'+images,img)

