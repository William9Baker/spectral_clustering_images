"""
接下来是将前面的预处理更改为同名，即不重命名操作，为此，在demo3_my_6077_test.py文件的基础上，新建spectral_clustering.py文件。

并对灰度化和压缩图像的代码文件进行重写，灰度化对应的代码文件是grayscale_processing.py，压缩图像的代码文件是picture_resize_2.py，
将这两个代码文件处理的时候不对图像进行重命名。
"""

# -*- coding: utf-8 -*-
from PCV.tools import imtools, pca
from PIL import Image, ImageDraw
from pylab import *
from scipy.cluster.vq import *
import os
import random


# imlist = imtools.get_imlist('./dir_my')
imlist = imtools.get_imlist('./dir_my_gray_rescale')
imnbr = len(imlist)

# Load images, run PCA.
immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')
V, S, immean = pca.pca(immatrix)

# Project on 2 PCs.
projected = array([dot(V[[0, 1]], immatrix[i] - immean)
                   for i in range(imnbr)])  # P131 Fig6-3左图
#projected = array([dot(V[[1, 2]], immatrix[i] - immean) for i in range(imnbr)])  # P131 Fig6-3右图

n = len(projected)
# compute distance matrix
S = array([[sqrt(sum((projected[i]-projected[j])**2))
            for i in range(n)] for j in range(n)], 'f')
# create Laplacian matrix
rowsum = sum(S, axis=0)
D = diag(1/sqrt(rowsum))
I = identity(n)
L = I - dot(D, dot(S,D))
# compute eigenvectors of L
U, sigma, V = linalg.svd(L)
k = 3
# create feature vector from k first eigenvectors
# by stacking eigenvectors as columns
features = array(V[:k]).T
# k-means
features = whiten(features)
centroids, distortion = kmeans(features,k)
code, distance = vq(features, centroids)

# plot clusters 绘制聚类簇
for c in range(k):
    ind = where(code == c)[0]   # where函数返回数组的索引值
    figure()   # 创建figure实例
    gray()
    for i in range(minimum(len(ind), 39)):
        # print(imlist[ind[i]])   # ./dir_my_gray_rescale\5.jpg
        im = Image.open(imlist[ind[i]])
        # print("im:%s" % im)  # im:<PIL.JpegImagePlugin.JpegImageFile image mode=L size=28x28 at 0x241B9DD2EF0>
        image_name = imlist[ind[i]].split("\\")[1]  # image_name: 5.jpg
        image_name_real = image_name.split(".")[0]  # image_name_real: 1_1
        image_name_new = image_name_real + ".png"
        # print(image_name_new)   # image_name_new: 1_1.png
        # print("image_name: %s" % image_name)
        # print("image_name_real: %s" % image_name_real)
        subplot(4, 10, i+1)
        imshow(array(im))   # 绘图
        # print("array(im)的值为%s" % array(im))

        # 使用imsave()函数保存图像
        pre_savename = "./dir_classfied_my/%02d/" % c   # "./dir/00"
        # savename = os.path.join(pre_savename, str(random.randint(0, 10000000)))
        savename = os.path.join(pre_savename, image_name_new)
        imsave(savename, array(im))

        axis('equal')
        axis('off')
show()