#-------------------------------------------#
# Code function: #
# Realize batch extraction of npy data as jpg #
# Just create the folder in advance and change the comment location path in the code #
#-------------------------------------------#
import os
import numpy as np
import argparse
from tqdm import tqdm
from skimage import io

base_path = './data/'        # The path of the original data contains 10 large folders. Each large folder contains npy files
new_path = './pic_data/'     # The big folder for saving pictures contains 10 folders. Each big folder contains three folders for train val test
name = os.listdir(base_path)

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='val')   # Select the mode before conversion, save it in the train folder and select train
opt = parser.parse_args()

for t in tqdm(name):
    file_name = opt.model + '_images.npy'
    np_path = os.path.join(base_path, t, file_name)

    data = np.load(np_path)
    print('The data contains %s pictures' % str(len(data)))

    print('Start conversion')
    for i in range (len(data)):
        pic = data[i].astype(np.uint8)
        fix = str(i+1) + '.png'
        save_path = os.path.join(new_path, t, opt.model, fix)
        io.imsave(save_path, pic)

    print('Conversion complete')
