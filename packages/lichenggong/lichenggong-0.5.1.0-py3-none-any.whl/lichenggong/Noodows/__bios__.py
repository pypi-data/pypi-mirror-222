# coding=utf-8
import gc, os, sys
import time as t

sys.path.append('../Program_Files/System')
import __logo__


def file_dir(files_dir):
    # 测量文件的路径与大小
    count = 0
    size = 0
    total_code_num = 0  # 统计文件代码行数计数变量
    total_blank_num = 0  # 统计文件空行数计数变量
    total_annotate_num = 0  # 统计文件注释行数计数变量
    file_list = []
    for parent, dir_names, filenames in os.walk(files_dir):
        for filename in filenames:
            if filename.endswith('.py'):
                file_list.append(os.path.join(parent, filename))
                # 将文件名和目录名拼成绝对路径，添加到列表里
            elif filename.endswith('.txt'):
                file_list.append(os.path.join(parent, filename))
                # txt文件存储也算上
    for root, dirs, files in os.walk(files_dir):
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
        count += len(files)
    for i in file_list:
        with open(i, encoding='UTF-8') as fp:
            code_num = 0  # 当前文件代码行数计数变量
            blank_num = 0  # 当前文件空行数计数变量
            annotate_num = 0  # 当前文件注释行数计数变量
            for content in fp.readlines():
                content = content.strip()
                # 统计空行
                if content == '':
                    blank_num += 1
                # 统计注释行
                elif content.startswith('#'):
                    annotate_num += 1
                # 统计代码行
                else:
                    code_num += 1
        total_code_num += code_num
        total_blank_num += blank_num
        total_annotate_num += annotate_num
    # 返回代码行数，空行数，注释行数
    num = [total_code_num, total_blank_num, total_annotate_num]
    files = [num, count, size]
    del size, count, fp, content, i
    del file_list, total_code_num, code_num, total_blank_num, blank_num, total_annotate_num, annotate_num
    gc.collect()
    return files


def bios():
    __logo__.logo3_0()
    file_name = r'../'
    scale = 20
    start = t.perf_counter()
    for i in range(scale + 1):
        a = "|" * i
        b = "-" * (scale - i)
        c = (i / scale) * 100
        dur = t.perf_counter() - start
        print("Loading {:^3.0f}%[{}{}]{:.2f}s Noodows is coming".format(c, a, b, dur))
    print()
    a = file_dir('../')
    print('代码行: {}'.format(a[0][0]))  # 返回代码行数
    print('空行数: {}'.format(a[0][1]))  # 返回空行数
    print('注释行: {}'.format(a[0][2]))  # 返回注释行数
    for root, dirs, file in os.walk(file_name):
        print('File folder：{0}'.format(root))
        print('Sub folders：{0}'.format(dirs))
        print('Files:{0}'.format(file))
        print('|' * 25)
    print('files:', a[1])
    print('large(MB)', a[2] / (1024 ** 2))
    print('hallo,world =) ')
    print()
    del a, root, dirs, file
    del i, scale, start, dur, b, c
    gc.collect()
