import requests
from lxml import etree
import re

def get_title(html):
    titles=html.xpath('//div[@class="detail-title"]/p/span/text()')
    i=1
    title_text=""
    for title in titles:
        title_text=title_text+title
        if i==1:
         title_text=title_text+" "
         i=i+1
    div_title=html.xpath('//div[@class="detail-title"]/text()')
    for title in div_title:
        title_text=title_text+title
        if i==1:
            title_text=title_text+" "
            i=i+1
    title_text=title_text.strip()
    print(">>title_text:",title_text)
    return title_text

def get_date(html):
    dates=html.xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[2]/span[2]/text()')
    i=1
    date_value=""
    for date in dates:
        date_value=date_value+date
    values=(date_value)
    s = values
    parts = s.split("：")
    date = parts[1] if len(parts) > 1 else None
    print(">>date:",date)
    return date

def get_clickid(news_link):
    pattern = r"\/(\d+)\.htm"  
    match = re.search(pattern, news_link)  
    clickid = match.group(1)
    print(">>clickid:",clickid) 
    return(clickid)

def get_clicks(clickid):
    url = f"https://www.yibinu.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid={clickid}&owner=1397404744&clicktype=wbnews"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
    res = requests.get(url=url, headers=header)
    print(">>clicks:",res.text)
    return res.text

def get_article(html):
    articles=html.xpath('//div[@class="v_news_content"]/p/text()')
    essays=''
    for article in articles:
        essays=essays+article
    articles=html.xpath('//div[@class="v_news_content"]/p/span/span/text()')
    for article in articles:
        essays=essays+article
    essays=essays.strip()
    print(">>article:",essays)
    return essays

def get_article_main(news_link):
    url=news_link
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}
    res = requests.get(url=url, headers=header)
    res.encoding = 'utf-8'
    html = res.text
    html = etree.HTML(html)

    #传参并调用
    article_title=get_title(html)
    article_date=get_date(html)
    clickid=get_clickid(news_link)
    article_clicks=get_clicks(clickid)
    article_text=get_article(html)
    return (article_title,article_date,article_clicks,article_text)

if __name__ == '__main__':
    news_link = "https://www.yibinu.edu.cn/info/1049/18652.htm"
    get_article_main(news_link)
    print("该片段仅用于测试，请运行'News_Spider'主程序.")



