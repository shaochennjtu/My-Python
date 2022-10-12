
with open('/home/samba/python/2月销售数据.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(f'{line}')

from pandas.io import json

#
# def read_data(self):
#     f = open('/home/cshao/1.txt', 'r', encoding='UTF-8')
#     read = f.readlines()
#     print(read)
