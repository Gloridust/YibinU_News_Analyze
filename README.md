# YibinU_News_Analyze
 宜宾学院新闻分析，包括新闻爬虫、热词、情感分析、数据可视化

## 程序结构

### News_Spider.py

1. 主程序结构

```python
import requests
from lxml import etree
import json
import csv
import os
```

```python
if __name__ == "__main__":

    page_links = get_page_links() #获取页面列表，返回一个含有各页面链接的列表

    for page_link in page_links: #从列表中遍历出每一个链接
        news_list = get_news_list(page_link) #传入页面链接，返回一个含有各新闻链接的列表

        for news_link in news_list: #从列表便利出每一篇新闻的链接
            article_title,article_date,article_clicks,article_text = get_article(news_link) #获取一篇新闻的 题目 日期 点击量 正文 
            write_to_csv(article_title,article_date,article_clicks,article_text)
```

1. 'get_page_links()'

功能：遍历页码列表，获取所有页码的新闻页面的链接。

传入参数：无

传出参数：'return(page_links)'

- 'page_links'：以列表(list)的形式返回页面链接列表，形如：

```python
['https://www.yibinu.edu.cn/xwzx/zhxw.htm','https://www.yibinu.edu.cn/xwzx/zhxw/44.htm','https://www.yibinu.edu.cn/xwzx/zhxw/43.htm']
```

这样的返回值。不难发现除了首页叫做'zhxw.htm'，其他的都是从最高页码到第一页命名。要求要自动获取最大页编号，自动化遍历。

2. 'get_news_lists(page_link)'

功能：获取单个页码对应的页面中，所有新闻的链接

传入参数：'page_link' 

传出参数：'return(news_links)'

- 'news_links' ：以列表(list)的形式返回各个新闻链接列表，形如：
```python
['https://www.yibinu.edu.cn/info/1049/62031.htm','https://www.yibinu.edu.cn/info/1049/62011.htm','https://www.yibinu.edu.cn/info/1049/61941.htm']
```

这样的返回值。

3. "get_article(news_link)"

功能：获取文章内容，包括：题目 日期 点击量 正文 

传入参数：'news_link'

传出参数：'return(article_title,article_date,article_clicks,article_text)'

- 'article_title'：文章标题
- 'article_date'：文章日期
- 'article_clicks'：文章点击量
- 'article_text'：文章正文

以上注意均格式化为字符串

