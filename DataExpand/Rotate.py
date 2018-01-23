# -*- coding:utf-8 -*-
import cv2
# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    # 返回旋转后的图像
    return rotated


def Rotate(image, angle, center=None, scale=1.0):

    # 获取图像尺寸
    (h, w) = image.shape[:2]
    if image.shape[2] == 3:
        constant = cv2.copyMakeBorder(image, int(h / 2), int(h / 2), int(w / 2), int(w / 2), cv2.BORDER_CONSTANT,
                                      value=[255, 255, 255])
        (nh, nw) = constant.shape[:2]
        # 若未指定旋转中心，则将图像中心设为旋转中心
        if center is None:
            center = (int(nw / 2), int(nh / 2))
        # 执行旋转

        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(constant, M, (nw, nh))
        # 返回旋转后的图像
        rotated = rotated[center[1] - int(h / 1.5): center[1] + int(h / 1.5), center[0] - int(w / 1.5): center[0] + int(w / 1.5)]
    else:
        if center is None:
            center = (w / 2, h / 2)
        # 执行旋转
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(image, M, (w, h))
    return rotated
