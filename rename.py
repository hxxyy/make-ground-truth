#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import glob
pathname = 'D:/Jinghang/sdk/Samples/VC/TwoCamera_VCDemo_Thread/Debug/1128/26/'

path_file_number = glob.glob(pathname=pathname+'/*.jpg')  # 获取当前文件夹下个数
print(len(path_file_number))
for i in range(1,len(path_file_number),2):
    src = pathname+ '  ('+ str(i) + ').jpg'
    dst = pathname+ '26_ ('+ str(i+1) + ').jpg'
    os.rename(src,dst)
    print(src)
    print(dst)
    print('----------')
    src = pathname+'  ('+ str(i+1) + ').jpg'
    dst = pathname+'26_ ('+ str(i) + ').jpg'
    os.rename(src,dst)
    print(src)
    print(dst)


