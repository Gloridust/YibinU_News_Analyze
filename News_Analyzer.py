from ltp import LTP
import pandas as pd  

ltp = LTP()    #path = "LTP/tiny" LTP/base|LTP/small|LTP/tiny

def read_from_excel(path):
    try:
        # 读取Excel文件
        df = pd.read_excel(path)
        # 将DataFrame转换为列表
        data_list = df.values.tolist()
        # 添加列名作为第一行
        header = df.columns.tolist()
        data_list.insert(0, header)
        return data_list
    except Exception as e:
        print("Error occurred while reading from Excel:", e)

def make_hot_people_dict(article):
    ## 命名实体识别
    result = ltp.pipeline([article], tasks = ["cws","ner"])
    print(result.ner)
    Nh_strings = [item[1] for sublist in result.ner for item in sublist if item[0] == 'Nh']
    print(Nh_strings)

    for name in Nh_strings:
        if name in hot_people_dict:
            hot_people_dict[name] += 1
        else:
            hot_people_dict[name] = 1
    print(hot_people_dict)
    return hot_people_dict

if __name__ == "__main__":
    data_list = read_from_excel("./data/articles-2023.xlsx")
    # print(data_list)
    titles_list = [row[0] for row in data_list]
    # print(titles_list)
    # dates_list = [row[1] for row in data_list[1:]]
    # clicks_list = [row[2] for row in data_list[2:]]
    articles_list = [row[3] for row in data_list[3:]]
    # print(articles_list)
    hot_people_dict={}
    for article in articles_list:
        hot_people_dict=make_hot_people_dict(article)
    hot_people_dict = sorted(hot_people_dict.items(), key=lambda x: x[1], reverse=True)
    print(">>活跃人物排序：",hot_people_dict)

    # 将排序后的字典写入 Excel 文件
    df = pd.DataFrame(hot_people_dict, columns=['姓名', '出现次数'])
    file_path = './data/sorted_hot_people-2023.xlsx'
    df.to_excel(file_path, index=False)