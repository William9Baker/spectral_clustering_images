"""
Python批量按比例缩小图片脚本分享
参考：https://m.jb51.net/article/66480.htm
"""

# -*- coding: cp936 -*-
# import Image
from PIL import Image
import glob, os

#图片批处理
def timage():
    for files in glob.glob('./dir_my_gray/*.png'):
        filepath,filename = os.path.split(files)
        filterame,exts = os.path.splitext(filename)
        #输出路径
        opfile = r'./dir_my_gray_rescale/'
        #判断opfile是否存在，不存在则创建
        if (os.path.isdir(opfile)==False):
            os.mkdir(opfile)
        im = Image.open(files)
        w,h = im.size
        im_ss = im.resize((28, 28))
        #im_ss = im.convert('P')
        # im_ss = im.resize((int(w*0.12), int(h*0.12)))
        im_ss.save(opfile+filterame+'.jpg')
        # im_ss.save(opfile + filterame + '.png')

if __name__=='__main__':
    timage()

    print('转换完毕')