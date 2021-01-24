# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/2/18 10:06
# Author    : 彭文瑜
# Site      : 
# File      : saveJsons.py
# Product   : PyCharm
# Project   : DataEnhancement
# explain   : 用于保存添加至背景的素材坐标以及标签


import json
def saveJson(filename,names):

    with open(filename, 'w') as file_obj:
        json.dump(names, file_obj)

        # # 写入文件
        # line = "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}\n".format(img_save_path, x1, y1, x2, y2,
        #                                      mark_x1, mark_y1, mark_x2, mark_y2,
        #                                      mark_x3, mark_y3, mark_x4, mark_y4)



if __name__ == "__main__":
    dic = {'name': '张三', 'age': '13'}

    saveJson("123.json",dic)