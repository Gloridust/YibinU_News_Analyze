import pandas as pd
from pyecharts.charts import Pie

# 读取Excel文件  
# 假设Excel文件名为'data.xlsx'，并且数据在第一个sheet中，列名为'Month'和'Value'  
df = pd.read_excel('../data/sorted_hot_people-cloud.xlsx', sheet_name=0)

# 提取列名和数据  
# 假设列名为'Month'和'Value'  
categories = df['姓名'].tolist()
values = df['出现次数'].tolist()

categories = categories[:10]
values = values[:10]

# 创建玫瑰饼图
def create_rose_pie(categories, values):
    pie = Pie()
    # 是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。
    # radius：扇区圆心角展现数据的百分比，半径展现数据的大小
    # area：所有扇区圆心角相同，仅通过半径展现数据大小
    pie.add("访问来源", [list(z) for z in zip(categories , values)], rosetype="area")
    pie.render("./html/charts/people_rose_pie_all.html")  # 渲染为HTML文件

# 调用函数创建玫瑰饼图
create_rose_pie(categories, values)