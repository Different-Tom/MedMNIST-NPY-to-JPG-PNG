#-------------------------------------------#
# 代码功能：                                  #
# 实现批量提取npy数据为jpg                      #
# 只需要提前创建文件夹 改动代码中的注释位置路径即可   #
#-------------------------------------------#
import os
import numpy as np
import argparse
from tqdm import tqdm
from skimage import io

base_path = './data/'        # 原始数据的路径 包含10个大文件夹 每个大文件夹下是npy文件
new_path = './pic_data/'     # 保存图片的大文件夹 包含10个文件夹 每个大文件夹下是train val test三个文件夹
name = os.listdir(base_path)

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='val')   # 转换之前选择模式 保存在train文件夹就选train
opt = parser.parse_args()

for t in tqdm(name):
    file_name = opt.model + '_images.npy'
    np_path = os.path.join(base_path, t, file_name)

    data = np.load(np_path)
    print('该数据包含%s张图片' % str(len(data)))

    print('开始转换')
    for i in range (len(data)):
        pic = data[i].astype(np.uint8)
        fix = str(i+1) + '.png'
        save_path = os.path.join(new_path, t, opt.model, fix)
        io.imsave(save_path, pic)

    print('转换完成')
