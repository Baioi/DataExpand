#coding=utf-8
from PIL import Image
def crop_image(img,img_path,a):
    # img = Image.open(img_path)
    h, w = img.shape[:2]  ##image2是交通标志图像
    # center =(w/2,h/2)
    box = (w*a,h*a,w*(1-a),h*(1-a))
    img.crop(box).save(img_path)



def crop_image(img_path,a,b):
    img = Image.open(img_path)
    box = (0,0,a,b)
    img.crop(box).save(img_path)


