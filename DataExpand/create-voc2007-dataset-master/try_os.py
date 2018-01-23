# -*- coding:utf-8 -*-
__auth__ = 'ytt'
'''
读取图片，重命名图片（即为将图片名称补全为6位），重命名json中图片的名称，生成train_ids.txt文件和test_ids.txt文件
'''

import re
import os
from PIL import Image

# 图片名称编号长度
name_length = 6

# Train Images 的位置
TRAIN_FILE = '/Users/ytt/myproject/TT100K/VOCdevkit/VOC2007/train'

# Test Images 的位
TEST_FILE = '/Users/ytt/myproject/TT100K/VOCdevkit/VOC2007/test'

# 图片所在位置
ORIGIN_IMAGES = '/Users/ytt/myproject/TT100K/VOCdevkit/VOC2007/JPEG'

# 输出文件
train_out = open('train.txt', 'w')

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
            new_name_txt = (name_length - len(str(old_name))) * '0' + str(old_name)

            #print new_name
            fullfilename = os.path.join(JPEG_path, Jname)
            os.chdir(JPEG_path)
            os.rename(fullfilename, new_name)
            train_out.write(new_name_txt+'\r\n')

    print "end"

# 处理Train
process(TRAIN_FILE)
# print name_number
train_out.close()








