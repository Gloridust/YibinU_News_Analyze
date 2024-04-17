import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.options import ItemStyleOpts
# 读取Excel文件的前20行数据
# 假设Excel文件名为'data.xlsx'，并且数据在第一个sheet中
df = pd.read_excel('../data/sorted_hot_people-2023.xlsx', engine='openpyxl', nrows=20)

# 获取列名和数据（假设有两列：'姓名'和'次数'）
columns = df['姓名'].tolist()
data = df['出现次数'].tolist()

# 确保数据长度不超过20，因为我们只读取了前20行
columns = columns[:20]
data = data[:20]


def create_bar_chart(columns, data):
    bar = Bar()
    bar.add_xaxis(columns)
    bar.add_yaxis(
        "出现次数",
        data,
        itemstyle_opts=ItemStyleOpts(color="#f075ab")  # 设置柱状图颜色为蓝色
    )
    bar.set_global_opts(title_opts=opts.TitleOpts(title="2023年度活跃人物"))
    bar.render("./html/people_name_bar_2023.html")


if __name__ == '__main__':
    create_bar_chart(columns, data)