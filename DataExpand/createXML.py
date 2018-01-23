import os
from create_Annotations import *


# xml文件规范定义
_INDENT = ' ' * 4
_NEW_LINE = '\n'
_FOLDER_NODE = 'VOC2007'
_ROOT_NODE = 'annotation'
_DATABASE_NAME = 'INRIA'
_CLASS = 'person'
_ANNOTATION = 'PASCAL VOC2007'
_AUTHOR = 'Peic'

_SEGMENTED = '0'
_DIFFICULT = '0'
_TRUNCATED = '0'
_POSE = 'Unspecified'

_IMAGE_PATH = 'JPEGImages'
_TXT_PATH = 'output.txt'
_ANNOTATION_SAVE_PATH = 'Annotations'

_IMAGE_CHANNEL = 3

if __name__ == '__main__':
    #转XML文件
    ouput_file = open(_TXT_PATH)
    current_dirpath = os.path.dirname(os.path.abspath('__file__'))

    if not os.path.exists(_ANNOTATION_SAVE_PATH):
        os.mkdir(_ANNOTATION_SAVE_PATH)

    lines = ouput_file.readlines()
    for line in lines:
        s = line.rstrip('\n')
        array = s.split(';')
        # 格式：name, class, xmin, ymin, xmax, ymax
        # [image];[x1];[y1];[x2];[y2];[class id];[superclass id];[pole id];[number on pole];[camera number];[frame number];[class label]
        attrs = dict()
        attrs['name'] = array[0]
        attrs['classification'] = array[11]
        attrs['xmin'] = array[1]
        attrs['ymin'] = array[2]
        attrs['xmax'] = array[3]
        attrs['ymax'] = array[4]

        # 构建XML文件名称
        xml_file_name = os.path.join(_ANNOTATION_SAVE_PATH, (attrs['name'].split('.'))[0] + '.xml')
        # print(xml_file_name)

        if os.path.exists( xml_file_name):
            # print('do exists')
            existed_doc = xml.dom.minidom.parse(xml_file_name)
            root_node = existed_doc.documentElement
            
            # 如果XML存在了, 添加object节点信息即可
            object_node = createObjectNode(existed_doc, attrs)
            root_node.appendChild(object_node)

            # 写入文件
            writeXMLFile(existed_doc, xml_file_name)
            
        else:
            # print('not exists')
            # 如果XML文件不存在, 创建文件并写入节点信息
            img_name = attrs['name']
            img_path = os.path.join(current_dirpath, _IMAGE_PATH, img_name)
            # 获取图片信息
            img = Image.open(img_path)
            width, height = img.size
            img.close()
            
            # 创建XML文件
            createXMLFile(attrs, width, height, xml_file_name)

