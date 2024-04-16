from ltp import LTP
import pandas as pd  

ltp = LTP()    #path = "LTP/tiny" LTP/base|LTP/small|LTP/tiny

def test():
    texts = "为提升全校师生国家安全意识，持续筑牢维护国家安全人民防线，营造和谐校园氛围，推动平安宜宾建设，近日，党委常委、副院长白玉林与我校40余名学生代表共同参加了由宜宾市委举办的2024年“国家安全宣传教育月”活动启动仪式。 夜幕降临，由我校学生主持的国家安全知识竞赛在合江门广场拉开了活动序幕，吸引了众多民众的参与。竞赛题目涵盖了国家安全法律法规、安全防范常识等多个方面，参赛者们积极抢答，展现了他们对国家安全知识的深厚积累和浓厚兴趣。 市委常委、政法委书记、秘书长刘晓卫作了重要讲话。在热烈的氛围中，刘晓卫、白玉林与各部门代表共同按下启动按钮，标志着宜宾市“国家安全宣传教育月” 活动正式拉开帷幕。 我校学生代表刘颖上台发言，分享了自己对国家安全的理解和认识。他表示，作为新时代的青年学子，应该努力提高科学知识水平，时刻绷紧国家安全这根弦，用行动回应习近平总书记对高校毕业生就业工作的殷殷关切，为维护国家安全贡献青春力量。此次活动，旨在增强我校学生主动参与国家安 全宣传教育活动的意识，提升同学们的安全责任和防范意识。宜宾学院将继续以此次活动为契机，深入开展国家安全宣传教育工作，为构建平安和谐的社会环境 贡献自己的力量。"
    ## 命名实体识别
    result = ltp.pipeline([texts], tasks = ["cws","ner"])
    print(result.ner)
    # [[('Ns', '宜宾市'), ('Ni', '促进会'), ('Ns', '宜宾'), ('Ni', '学院'), ('Nh', '白玉林'), ('Ni', '宜宾市市场监督管理局'), ('Nh', '宿斌'), ('Ni', '标促会'), ('Nh', '赵东'), ('Ni', '标促会'), ('Ni', '宜宾市市场监管局标准化科'), ('Nh', '王顺强')]]
# test()

def read_from_excel():
    try:
        # 读取Excel文件
        df = pd.read_excel("./data/articles.xlsx")
        # 将DataFrame转换为列表
        data_list = df.values.tolist()
        # 添加列名作为第一行
        header = df.columns.tolist()
        data_list.insert(0, header)
        return data_list
    except Exception as e:
        print("Error occurred while reading from Excel:", e)


if __name__ == "__main__":
    data_list = read_from_excel()
    print(data_list)
    titles_list = [row[0] for row in data_list]
    dates_list = [row[1] for row in data_list[1:]]
    clicks_list = [row[2] for row in data_list[2:]]
    articles_list = [row[3] for row in data_list[3:]]
    print(articles_list)