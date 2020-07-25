"""
其中灰度化的过程中仿照压缩图像的代码文件picture_resize_2.py，新建grayscale_processing_2.py文件。

"""

# -*- coding: cp936 -*-
# import Image
from PIL import Image
import glob, os
import cv2


#图片批处理
def timage():
    for files in glob.glob('./dir_my/*.png'):
        filepath,filename = os.path.split(files)
        filterame,exts = os.path.splitext(filename)
        #输出路径
        opfile = r'./dir_my_gray/'
        #判断opfile是否存在，不存在则创建
        if (os.path.isdir(opfile)==False):
            os.mkdir(opfile)
        # im = Image.open(files)
        im = cv2.imread(files)
        GrayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        # w,h = im.size
        # im_ss = im.resize((28, 28))
        # #im_ss = im.convert('P')
        # # im_ss = im.resize((int(w*0.12), int(h*0.12)))
        # # im_ss.save(opfile+filterame+'.jpg')

        # GrayImage.save(opfile + filterame + '.png')
        cv2.imwrite("./dir_my_gray/{}.png".format(str(filterame)), GrayImage)

if __name__=='__main__':
    timage()

    print('转换完毕')