# -*- coding:gbk -*-
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

# ��ȡExcel�ļ�
df = pd.read_excel('sorted_hot_people-cloud.xlsx', engine='openpyxl')

# ��ȡ�����ͳ��ִ���
names = df['����'].tolist()
frequencies = df['���ִ���'].tolist()

# �������ͳ��ִ����ϲ��ɴ�Ƶ�ֵ�
word_freq = {name: freq for name, freq in zip(names, frequencies)}

# �������ƶ���
wordcloud = (
    WordCloud()
        .add(
        "",
        list(word_freq.items()),
        word_size_range=[20, 100],
        shape=SymbolType.DIAMOND  # ����������״������ 'circle'
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="�����ȶ�����"))
)

# ��Ⱦ����ͼ��HTML�ļ�
wordcloud.render("2022-2024���������.html")