# -*- coding:utf-8 -*-
import cv2
import numpy as np
import math
# 定义旋转rotate函数
def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]
    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)
    # 执行旋转]
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    # 返回旋转后的图像
    return rotated


def Rotate(image, angle, center=None, scale=1.0):

    # 获取图像尺寸
    (h, w) = image.shape[:2]
    if image.shape[2] == 3:
        '''
        constant = cv2.copyMakeBorder(image, int(h / 2), int(h / 2), int(w / 2), int(w / 2), cv2.BORDER_CONSTANT,
                                      value=[255, 255, 255])
        (nh, nw) = constant.shape[:2]
        # 若未指定旋转中心，则将图像中心设为旋转中心
        if center is None:
            center = (int(nw / 2), int(nh / 2))
        # 执行旋转

        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(constant, M, (nw, nh))
        cv2.imshow('rotated', rotated)
        # 返回旋转后的图像
        rotated = rotated[center[1] - int(h / 1.5): center[1] + int(h / 1.5), center[0] - int(w / 1.5): center[0] + int(w / 1.5)]
        '''
        rangle = np.deg2rad(angle)  # angle in radians
        # now calculate new image width and height
        nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
        nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0,2] += rot_move[0]
        rot_mat[1,2] += rot_move[1]
        return cv2.warpAffine(image, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4, borderValue =(255, 255, 255))
    else:
        if center is None:
            center = (w / 2, h / 2)
        # 执行旋转
        rangle = np.deg2rad(angle)  # angle in radians
        # now calculate new image width and height
        nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
        nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0,2] += rot_move[0]
        rot_mat[1,2] += rot_move[1]
        return cv2.warpAffine(image, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4, borderValue =(255, 255, 255))
        rotated = cv2.warpAffine(image, M, (w, h), borderValue =(255, 255, 255))
    return rotated