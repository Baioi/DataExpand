#coding=utf-8
import cv2
# 定义缩放resize函数
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    inter_methods = [
        ("cv2.INTER_NEAREST", cv2.INTER_NEAREST), ##最近邻插值法
        ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),##双线性插值
        ("cv2.INTER_AREA", cv2.INTER_AREA), ##使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..
        ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),##立方插值
        ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
    # 初始化缩放比例，并获取图像尺寸
    dim = None
    (h, w) = image.shape[:2]
    # 如果宽度和高度均为0，则返回原图
    if width is None and height is None:
        return image
    # 宽度是0
    if width is None:
        # 则根据高度计算缩放比例
        r = height / float(h)
        dim = (int(w * r), height)
    # 如果高度为0
    else:
        # 根据宽度计算缩放比例
        r = width / float(w)
        dim = (width, int(h * r))
    # 缩放图像
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
    # 返回缩放后的图像
    return resized

##图像长宽缩放，a是缩放银子，a大于1，是扁的椭圆，a小于1,是长的椭圆
def deformation(image,a):
    dim = None
    (h, w) = image.shape[:2]
    # 如果宽度和高度均为0，则返回原图
        # 根据宽度计算缩放比例
    width = int(w * a)
    dim = (width, h)
    # 缩放图像
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
    # 返回缩放后的图像
    return resized
