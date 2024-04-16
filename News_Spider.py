import requests
from lxml import etree
import json
import csv
import os

def get_page_links():
    page_links=[]
    url = "https://www.yibinu.edu.cn/xwzx/zhxw.htm"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
    html = requests.get(url=url,headers=header)
    #print(html.status_code)
    html = html.text
    # print(html)
    html = etree.HTML(html)
    # print(html)
    #html1 = html.xpath("//span[@class='p_no']/a/@href")
    html2 = html.xpath("/html/body/div[4]/div/div[2]/div[3]/div/span[2]/span[4]/a/@href") ##输出结果为第二页网址
    #print(html2)
    for page_link in html2:
        data = f"{page_link}"
        list = []
        list.append(data.replace("/44",""))
        for i in range(44,0,-1):
            result = data.replace("44",f"{i}")
            list.append(result)
        list1 = list
        #print(list)
        for page_link1 in list1:
            page_url = "https://www.yibinu.edu.cn/xwzx/"+page_link1
            print(page_url)
            page_links.append(page_url)
    return(page_links)

def get_news_lists(page_link):
    article_list=[]
    url = page_link
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
    res = requests.get(url=url, headers=header)
    print(res.status_code)
    res.encoding = "utf-8"
    html = res.text
    html = etree.HTML(html)
    srcs = html.xpath("//div[@class='title']/a/@href")
    for i in srcs:
        article_link = "https://www.yibinu.edu.cn" + i[2::]
        article_list.append(article_link)
        # print(article_link)
    return(article_list)

def get_article(news_link):
    pass

def write_to_csv(article_title, article_date, article_clicks, article_text):
    # 检查文件是否存在，如果不存在则创建文件并写入表头
    file_exists = os.path.isfile('./data/articles.csv')
    with open('./data/articles.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['article_title', 'article_date', 'article_clicks', 'article_text'])
        # 将文章信息写入CSV文件
        writer.writerow([article_title, article_date, article_clicks, article_text])


if __name__ == "__main__":
    #获取页面列表，返回一个含有各页面链接的列表
    page_links = get_page_links()
    #从列表中遍历出每一个链接
    for page_link in page_links:
        #传入页面链接，返回一个含有各新闻链接的列表
        news_list = get_news_lists(page_link)
        #传入页面链接，返回一个含有各新闻链接的列表
        for news_link in news_list:
            #获取一篇新闻的 题目 日期 点击量 正文 
            article_title,article_date,article_clicks,article_text = get_article(news_link)
            write_to_csv(article_title,article_date,article_clicks,article_text)