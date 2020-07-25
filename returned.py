"""
由于聚类后图像名称有所变化，故先做test测试文件，新建returned_test.py文件，各文件夹和真实保持一致

"""
import os
import glob
import shutil


PATH_0 = './dir_my/'  # 存放原始图像的文件夹路径
PATH_1 = './dir_classfied_my/'  # 存放根据聚类效果来对原始图像重新排布的原始图像文件夹路径
# 1、先遍历图像处理前总文件夹的图像文件
for filename_0 in os.listdir(r"./dir_my"):      # listdir的参数是文件夹的路径
    # print(filename_0)        #此时的filename是文件夹中文件的名称
    for filename_1 in os.listdir(r"./dir_classfied_my"):
        # print(filename_1)  #  filename_1: 00 01 02
        for filename_2 in os.listdir(r"./dir_classfied_my/%s" % filename_1):
            # print(filename_2)    # filename_2: '1_2.jpg'

            paths = PATH_0 + filename_1 + '/' + filename_2
            # print(paths)
            if filename_2 == filename_0:
                shutil.copy(os.path.join(PATH_0, filename_0), os.path.join(PATH_1, filename_1, filename_0))
