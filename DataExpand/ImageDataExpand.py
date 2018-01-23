#coding=utf-8
import numpy as np
import cv2
import os
import string
import random
from Resize import deformation
from Resize import resize
from Rotate import Rotate,rotate
from LightChang import ChangeLightPower
import random
from ImagesFusion import Images_fusion
from MinOutRect import Min_out_rect
import create_Annotations as ano
import xml.dom
import xml.dom.minidom
from PIL import Image
"""
图像的随机（在一定范围内）旋转，缩放，光照强度变化
"""


##图像中心
def findCenter(img):
    (h, w) = img.shape[:2]
    center = (w/2, h/2)
    return center


def contains(ind, x_1, y_1, x_2, y_2, boxpack):
    boxes = boxpack[ind]
    for box in boxes:
        maxx = min(box[2], x_2)
        maxy = min(box[3], y_2)
        minx = max(box[0], x_1)
        miny = max(box[1], y_1)
        if minx > maxx or miny > maxy:
            continue
        else:
            return True
    return False


if __name__ == "__main__":
    images_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/NEW1'
    file_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad-all1'
    out_path1 = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad1'
    out_path2 = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/NEW1'
    """以下用于生成更多的交通标志，变大变小，旋转光照也做一些变化等"""
    # image_name = os.listdir(file_path)
    # for images in image_name:
    #     name = images.split('.')
    #     ext = name[len(name)-1]
    #     img_name = ""
    #     for i in range(len(name)-1):
    #         img_name += name[i]
    #     img_path = os.path.join(file_path, images)
    #     img = cv2.imread(img_path,-1)
    #     # win1 = cv2.namedWindow('Original', flags=0)
    #     # cv2.imshow("Original",img)
    #     image_file_path = os.path.join(out_path1, img_name)
    #     isExists = os.path.exists(image_file_path)
    #     if not isExists:
    #         os.makedirs(image_file_path)
    #         print(image_file_path+'创建成功')
    #     else:
    #         print(image_file_path+'已经存在')
    #
    #     for i in range(0, 1000):
    #         x = random.randint(-10, 10)
    #         y = random.randint(55, 460)
    #         a = random.uniform(0.7, 1.2)
    #         if ext == 'jpg':
    #             image = Rotate(img, x)
    #         else:
    #             image = rotate(img,x)
    #         image = resize(image, width=y, height=None)
    #         image = deformation(image, a)
    #         light = random.uniform(0.6, 2)
    #         image = ChangeLightPower(image, light)
    #         # light_a = random.normalvariate(0.88,1.2)
    #         # light_b = random.uniform(-10,10)
    #         # image = ChangeLightPower(image,light_a,light_b)
    #         # h, w = image.shape[:2]
    #         # image = image[int(w*0.12):int(w*0.95),int(h*0.1):int(h*0.93)]
    #         cv2.imwrite(image_file_path+'/'+str(i)+'.png', image)

    """以下用以将交通标志图标和街景图融合在一起，写出XML"""
    Traffic_signs = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/data/marks/pad1'
    Street_views = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/NEW2'
    output_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/创造的图像数据'
    out_xml_path = '/home/ytt/misc/ytt/下载/datasets/Tencent_Traffin_Sign_DataSets/创造的图像数据/XML'
    Traffic_sign_files = os.listdir(Traffic_signs)
    Street_vies_image = os.listdir(Street_views)
    street_list = [0] * len(Street_vies_image)
    street_boxes = []
    for i in range(len(Street_vies_image)):
        street_boxes.append([])
    # TO DO: 不能让同一个图上贴很多交通标志&同样的交通标志 解决
    # 交通标志不能重叠 解决（使用street_boxes，判断矩形是否相交）
    # 交通标志的数量 解决
    num = {}
    f_num = open('num.txt', 'r')
    f_out = open('statistic.txt', 'w')
    lines = f_num.readlines()
    for line in lines:
        strings = line.split(' ')
        num[strings[2]] = 1000 - string.atoi(strings[0])
        if num[strings[2]] < 0:
            temp = 1000 - num[strings[2]]
            f_out.write(strings[2] + " " + str(temp) + "\n")
    for images_file in Traffic_sign_files:
        print images_file
        images = os.listdir(os.path.join(Traffic_signs, images_file))

        # 处理数量，公式为1000-原数据集数量，结果保存在statistic.txt
        amount = num[images_file]
        f_out.write(images_file + " " + str(amount) + "\n")
        used = []
        t = 0
        for traffic_sign in images:
            print t
            t += 1
            street_img = random.sample(Street_vies_image, 1)[0]
            # print street_img
            # print Street_vies_image.index(street_img)
            # print street_boxes[Street_vies_image.index(street_img)]

            # 条件：同一个街景图中的标志最多8个  同一个交通标志不能出现在同一个街景图中
            while street_list[Street_vies_image.index(street_img)] > 8 or street_img in used:
                street_img = random.sample(Street_vies_image, 1)[0]

            used.append(street_img)

            # 为了使同一个标志能够在一张街景图片中共存，改变街景图片的输入路径为输出路径，否则原图像会被覆盖
            if street_list[Street_vies_image.index(street_img)] == 0:
                street_img_path = os.path.join(Street_views, street_img)
            else:
                street_img_path = os.path.join(output_path, street_img)
            street_list[Street_vies_image.index(street_img)] += 1

            traffic_sign_path = os.path.join(Traffic_signs, images_file, traffic_sign)
            x1, y1, x2, y2 = Min_out_rect(traffic_sign_path)
            w = cv2.imread(traffic_sign_path, -1).shape[1]
            h = cv2.imread(traffic_sign_path, -1).shape[0]
            street_image = cv2.imread(street_img_path)
            sz = street_image.shape
            a = int(random.uniform(100, sz[1]-(w+1)))
            b = int(random.uniform(100, sz[0]-(h+1)))
            a1 = x1 + a
            a2 = x2 + a
            b1 = y1 + b
            b2 = y2 + b
            # 判断是否区域内有其他标志
            # contains: i, a1, b1, a2, b2, street_boxes
            # return boolean
            tempnum = 0
            while contains(Street_vies_image.index(street_img), a1, b1, a2, b2, street_boxes):
                a = int(random.uniform(w+1, sz[1] - (w+1)))
                b = int(random.uniform(h+1, sz[0] - (h+1)))
                a1 = x1 + a
                a2 = x2 + a
                b1 = y1 + b
                b2 = y2 + b
                tempnum += 1
                if tempnum > 10:
                    print "boxes in " + street_img + ":"
                    print Street_vies_image.index(street_img)
                    print "\n"
                    exit(1)
            street_boxes[Street_vies_image.index(street_img)].append([a1, b1, a2, b2])
            # 注意图像与矩阵的对应关系
            Images_fusion(street_img_path, traffic_sign_path,
                          a, b, outputfile=os.path.join(output_path, street_img))
            """写入XML的程序"""
            attrs = dict()
            attrs['name'] = street_img
            attrs['classification'] = images_file
            attrs['xmin'] = str(a1)
            attrs['ymin'] = str(b1)
            attrs['xmax'] = str(a2)
            attrs['ymax'] = str(b2)

            xml_file_name = os.path.join(out_xml_path, (attrs['name'].split('.'))[0] + '.xml')
            # print(xml_file_name)
            if os.path.exists(xml_file_name):
                # print('do exists')
                existed_doc = xml.dom.minidom.parse(xml_file_name)
                root_node = existed_doc.documentElement

                # 如果XML存在了, 添加object节点信息即可
                object_node = ano.createObjectNode(existed_doc, attrs)
                root_node.appendChild(object_node)

                # 写入文件
                ano.writeXMLFile(existed_doc, xml_file_name)

            else:
                # print('not exists')
                # 如果XML文件不存在, 创建文件并写入节点信息
                img_name = attrs['name']
                img_path = os.path.join(output_path, img_name)
                # 获取图片信息
                img = Image.open(img_path)
                width, height = img.size
                img.close()

                # 创建XML文件
                ano.createXMLFile(attrs, width, height, xml_file_name)
            if t >= amount:
                break
    #     if cv2.waitKey(0) & 0xFF == ord('q'):
    #         break
    # cv2.destroyAllWindows()
