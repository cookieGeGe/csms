# -*- coding: utf-8 -*- 
# @Time : 2019/9/18 8:37 
# @Author :  
# @Site :  
# @File : image_test.py 
# @Software: PyCharm
import time
from PIL import Image
import os


class CompressImage(object):

    def __init__(self, infile):
        self.infile = infile
        self.dir = os.path.dirname(self.infile)
        self.resize_file = None
        self.outfile = None
        self.get_outfile()
        self.get_resize_file()

    def get_size(self, file):
        # 获取文件大小:KB
        size = os.path.getsize(file)
        return size / 1024

    # def get_outfile(self):
    #     # dir = os.path.dirname(self.infile)
    #     suffix = 'min_' + os.path.basename(self.infile)
    #     self.outfile = os.path.join(self.dir, suffix)

    def get_outfile(self):
        templist = self.infile.split('.')
        self.outfile = templist[0] + '_min.' + templist[1]

    def get_resize_file(self):
        # dir = os.path.dirname(self.infile)
        suffix = 'resize_' + os.path.basename(self.infile)
        self.resize_file = os.path.join(self.dir, suffix)

    def compress_image(self, mb=100, step=10, quality=80):
        """不改变图片尺寸压缩到指定大小
        :param infile: 压缩源文件
        :param outfile: 压缩文件保存地址
        :param mb: 压缩目标，KB
        :param step: 每次调整的压缩比率
        :param quality: 初始压缩比率
        :return: 压缩文件地址，压缩文件大小
        """
        o_size = self.get_size(self.infile)
        # print(o_size)
        if o_size <= mb:
            im = Image.open(self.infile)
            im.save(self.outfile, quality=quality)
            return self.outfile
        while o_size > mb:
            im = Image.open(self.resize_file)
            im.save(self.outfile, quality=quality)
            if quality - step < 0:
                print(quality - step)
                break
            quality -= step
            o_size = self.get_size(self.outfile)
            # print(o_size)
        return self.outfile

    def resize_image(self, x_s=200):
        """修改图片尺寸
        :param infile: 图片源文件
        :param outfile: 重设尺寸文件保存地址
        :param x_s: 设置的宽度
        :return:
        """
        im = Image.open(self.infile)
        x, y = im.size
        y_s = int(y * x_s / x)
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        out.save(self.resize_file)

    def remove(self):
        if os.path.exists(self.resize_file):
            os.remove(self.resize_file)

    def default_compress_image(self):
        self.resize_image()
        self.compress_image()
        self.remove()
        return self.outfile


def get_all_files(path):
    temp_list = []
    dir_list = os.listdir(path)
    for temp_dir in dir_list:
        temp_path = os.path.join(path, temp_dir)
        if os.path.isdir(temp_path):
            temp_list.extend(get_all_files(temp_path))
        else:
            files = temp_path.split('.')
            file_list = ['jpg', 'jpeg', 'png', 'gif']
            if len(files) < 2:
                continue
            if temp_path.find('min') != -1:
                continue
            if files[-1].lower() in file_list:
                temp_list.append(temp_path)
    return temp_list

# compress = CompressImage(r'C:\Users\PC-00005\Pictures\Saved Pictures\14779.jpg')
# print(compress.default_compress_image())
# a='123456'
# b='123'
# print(a.index(b))
# print(a.replace(b, ''))


# if __name__ == '__main__':
#     # path = r'C:\Users\zhang\Desktop\csms-0923\static\media\project'
#     path = r'/home/app/csms/static/media'
#     img_list = get_all_files(path)
#     for img in img_list:
#         try:
#             compress = CompressImage(img)
#             print(compress.default_compress_image())
#         except Exception as e:
#             print(e)
#             pass
