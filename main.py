'''

面向对象：14数据分析案例，主业务逻辑代码
实现步骤
1. 设计一个类，可以完成数据的封装      #data_define.py
2. 设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3. 读取文件，生产数据对象
4. 进行数据需求的逻辑计算（计算每一天的销售额）
5. 通过PyEcharts进行图形绘制

'''
# from typing import List
from typing import List

from file_define import FileReader, TextFileReader
from data_define import Record
from pyecharts.charts import  Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reader = TextFileReader('/home/samba/python/1月销售数据.txt')
# json_file_reader = JsonileReader('/home/samba/python/1月销售数据.txt')


jan_data: List[Record]= text_file_reader.read_data()
# feb_data: List[Record]= json_file_reader.read_data()


data_dict = {}
for record in jan_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

# print(data_dict)

# 可视化图标开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))        #添加x轴数据
bar.add_yaxis('销售额', list(data_dict.values()))     #添加y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title='每日销售额')
)

bar.render('每日销售额柱状图.html')
