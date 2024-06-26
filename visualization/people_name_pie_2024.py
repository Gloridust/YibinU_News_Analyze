import pandas as pd
from pyecharts.charts import Pie

# 读取Excel文件
# 假设Excel文件名为'data.xlsx'，并且数据在第一个sheet中，列名为'Month'和'Value'
df = pd.read_excel('../data/sorted_hot_people-2024.xlsx', sheet_name=0)

# 提取列名和数据
# 假设列名为'Month'和'Value'
categories = df['姓名'].tolist()
values = df['出现次数'].tolist()

categories = categories[:10]
values = values[:10]

pie = Pie()
pie.add("访问来源",[list(z) for z in zip(categories, values)],)
pie.render("./html/charts/people_name_pie_2024.html")
