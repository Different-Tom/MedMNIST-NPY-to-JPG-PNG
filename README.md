# MedMNIST-NPY-to-JPG-or-PNG
Researchers at Shanghai Jiaotong University created a new open medical image data set MedMNIST and designed the "MedMNIST Classification Decathlon" to promote the research of AutoML algorithms in the field of medical image analysis. But their data set is in Npy file format. I help you to extract npy into png, jpg and other file formats, which can facilitate the experimentation of researchers.


Run pic_ ex.py file is OK, there are relevant notes in it.


Environment: 
Python 3.6

numpy==1.16.0

scikit-image==0.17.2

tqdm==4.52.0

And then the directory structure
1.pic_ ex.py
2.data

There are ten folders with NPY files inside
3.pic_ data

The following contains ten categories of folder to extract pictures, and each folder has three folders: test, train and val
