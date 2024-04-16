from ltp import LTP
import pandas as pd  

ltp = LTP()    #path = "LTP/tiny" LTP/base|LTP/small|LTP/tiny

def test():
    texts = "3月20日，宜宾市标准化促进会（以下简称“标促会”）第二届第一次会员大会暨换届大会在宜宾学院召开。学校党委常委、副院长白玉林，宜宾市市场监督管理局局长宿斌，标促会新任理事长赵东、标促会部分会员代表等100余人参加会议。会议由宜宾市市场监管局标准化科科长王顺强主持。"
    ## 命名实体识别
    result = ltp.pipeline([texts], tasks = ["cws","ner"])
    print(result.ner)
    # [[('Ns', '宜宾市'), ('Ni', '促进会'), ('Ns', '宜宾'), ('Ni', '学院'), ('Nh', '白玉林'), ('Ni', '宜宾市市场监督管理局'), ('Nh', '宿斌'), ('Ni', '标促会'), ('Nh', '赵东'), ('Ni', '标促会'), ('Ni', '宜宾市市场监管局标准化科'), ('Nh', '王顺强')]]


def read_csv():
    # 读取CSV文件  
    df = pd.read_csv('./data/articles.csv')  
      
    # 提取所需列，并将它们转换为列表  
    articles = []  
    for index, row in df.iterrows():  
        article = {  
            'article_title': row['article_title'],  
            'article_date': row['article_date'],  
            'article_clicks': row['article_clicks'],  
            'article_text': row['article_text']  
        }  
        articles.append(article)  
      
    # 返回包含所有文章的列表  
    return articles  
  
# 调用函数并打印结果  
articles_list = read_csv()  
for article in articles_list:  
    print(article)