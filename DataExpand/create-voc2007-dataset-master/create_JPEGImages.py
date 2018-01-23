# -*- coding:utf-8 -*-

__auth__ = 'ytt'

'''
读取图片，重命名图片（即为将图片名称补全为6位），重命名json中图片的名称，生成train_ids.txt文件和test_ids.txt文件
'''

import re
import os
from PIL import Image
import json

# 图片名称起始编号
#global name_number
# 图片名称编号长度
name_length = 6

# Train Images 的位置
TRAIN_ANNO = r'G:\pycharm\INRIA2VOC\INRIADATA\original_images\Train\annotations'

# Test Images 的位置
TEST_ANNO = r'G:\pycharm\INRIA2VOC\INRIADATA\original_images\Test\annotations'

# 图片所在位置
ORIGIN_IMAGES = '/Users/ytt/myproject/TT100K/VOCdevkit/VOC2007/JPEGImages'

# 输出文件
fout = open('output.txt', 'w')

#创建另存为的文件夹
# if not os.path.exists('JPEGImages1'):
#     os.mkdir('JPEGImages1')
#     print "mkdir donw"

# 定义处理函数
def process(JPEG_path):
    pic_ext = ['jpg']
    JPEG_file_names = os.listdir(JPEG_path)
    #print JPEG_file_names
    for Jname in JPEG_file_names:
        ext = Jname.split(".")[1]
        #print ext
        if ext in pic_ext:
            old_name = Jname.split(".")[0]
            #print len(old_name)
            # 构建新的图片名称
            new_name = (name_length - len(str(old_name)))* '0' + str(old_name) + '.jpg'
            #print new_name
            #os.rename(Jname, new_name)
            image = Image.open(os.path.join(ORIGIN_IMAGES, Jname))
            image.save(os.path.join("JPEGImages1", new_name), 'jpeg')




    # print "process \n{} \ndone".format(anno_path)



# 处理Train
process(ORIGIN_IMAGES)
# print name_number



#fout.close()








