import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

df = pd.read_excel('../data/sorted_hot_people-cloud.xlsx', engine='openpyxl')

names = df['姓名'].tolist()
frequencies = df['出现次数'].tolist()

word_freq = {name: freq for name, freq in zip(names, frequencies)}

wordcloud = (
    WordCloud()
        .add(
        "",
        list(word_freq.items()),
        word_size_range=[20, 100],
        shape=SymbolType.DIAMOND
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="2022-2024人物活跃度词云"))
)

wordcloud.render("./html/people_name_cloud_all.html")