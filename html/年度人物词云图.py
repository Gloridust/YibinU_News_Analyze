# -*- coding:gbk -*-
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# 读取Excel文件
df = pd.read_excel('sorted_hot_people-cloud.xlsx', engine='openpyxl')

# 提取姓名和出现次数
names = df['姓名'].tolist()
frequencies = df['出现次数'].tolist()

# 将姓名和出现次数合并成词频字典
word_freq = {name: freq for name, freq in zip(names, frequencies)}

# 创建词云对象
wordcloud = (
    WordCloud()
        .add(
        "",
        list(word_freq.items()),
        word_size_range=[20, 100],
        shape=SymbolType.DIAMOND  # 或者其他形状，比如 'circle'
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="三年热度人物"))
)

# 渲染词云图到HTML文件
wordcloud.render("2022-2024年年度人物.html")