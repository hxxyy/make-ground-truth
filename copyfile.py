#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import glob
from shutil import copyfile

for j in (range(26,27)):
    print(j)
    pathname = 'D:/Jinghang/sdk/Samples/VC/TwoCamera_VCDemo_Thread/Debug/1128/aligned/' + str(j) + '/'
    pathname2 = 'D:/Jinghang/sdk/Samples/VC/TwoCamera_VCDemo_Thread/Debug/1128/aligned/' + str(j*10) + '/'

    path_file_number = glob.glob(pathname=pathname+'/*.png')  # 获取当前文件夹下个数
    n = 1
    for i in range(1,len(path_file_number),14):
        for k in range(10):
            src = pathname+ str(j)+'_ ('+ str(i) + ').png'
            dst = pathname2+ str(j)+'_ ('+ str(n) + ').png'
            copyfile(src, dst)
            n = n+1
            i += 1

        src = pathname+ str(j)+'_ ('+ str(i-6) + ').png'
        dst = pathname2+ str(j)+'_ ('+ str(n) + ').png'
        copyfile(src,dst)
        n = n+1

        src = pathname + str(j) + '_ (' + str(i-5) + ').png'
        dst = pathname2 + str(j) + '_ (' + str(n) + ').png'
        copyfile(src, dst)
        n = n + 1

        for k in range(4):
            src = pathname + str(j) + '_ (' + str(i) + ').png'
            dst = pathname2 + str(j) + '_ (' + str(n) + ').png'
            copyfile(src, dst)
            n = n + 1
            i += 1

        src = pathname+ str(j)+'_ ('+ str(i-10) + ').png'
        dst = pathname2+ str(j)+'_ ('+ str(n) + ').png'
        copyfile(src,dst)
        n = n+1

        src = pathname + str(j) + '_ (' + str(i-9) + ').png'
        dst = pathname2 + str(j) + '_ (' + str(n) + ').png'
        copyfile(src, dst)
        n = n + 1
