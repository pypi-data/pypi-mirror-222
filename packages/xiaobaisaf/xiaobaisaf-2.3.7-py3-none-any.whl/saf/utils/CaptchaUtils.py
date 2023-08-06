#! /usr/bin/env python
'''
@Author: xiaobaiTser
@Time  : 2022/8/24 1:37
@File  : image_utils.py
'''
import os

import cv2
import numpy as np
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from saf import WebDriver, By, DdddOcr, WebElement
from saf.utils.ElementUtils import find_element

def image2str(driver: WebDriver = None, by: str = By.XPATH,value: str = ''):
    '''
    图片验证码识别工具
    :param driver   : 浏览器驱动
    :param by       : 定位方法
    :param value    : 定位表达式
    :return         : 返回验证码图片中识别的字符串
    '''
    return DdddOcr(show_ad=False).classification(find_element(driver, by, value=value).screenshot_as_base64)

def checkSlider(driver: WebDriver = None, target_element: WebElement = None, background_element: WebElement = None,
                button_element: WebElement = None):
    '''
    滑块验证码识别工具，基于openCV识别图片及图片二次处理
    :param driver               : 浏览器驱动
    :param target_element       : 目标图片（小图）
    :param background_element   : 背景图片（大图）
    :param button_element       : 滑块按钮
    :return:
    '''
    ''' 获取验证码的小图与背景图 '''
    dd = DdddOcr(show_ad=False, det=False, ocr=False)

    target_element.screenshot('target.png')
    with open('target.png', 'rb') as f:
        target = f.read()

    background_element.screenshot('background.png')

    '''  因为背景图是直接截图的所以匹配的结果是不准确的，需要去除  '''
    img = cv2.imread('background.png')
    template = cv2.imread('target.png')
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8

    loc = np.where(res >= threshold)

    w, h = template.shape[:-1]
    for pt in zip(*loc[::-1]):
        img[pt[1]:pt[1]+h, pt[0]:pt[0]+w] = 0

    cv2.imwrite('background_new.png', img)

    sleep(2)

    ''' 在处理之后的图片中进行查询坐标的操作 '''
    with open('background_new.png', 'rb') as f:
        background = f.read()

    result = dd.slide_match(target_bytes=target, background_bytes=background, simple_target=True)

    action = ActionChains(driver)
    action.click_and_hold(on_element=button_element).\
        move_by_offset(xoffset=result['target'][0], yoffset=0).\
        release().\
        perform()

    ''' 验证码通过之后，打扫战场，删除图片文件 '''
    os.remove('target.png')
    os.remove('background.png')
    os.remove('background_new.png')