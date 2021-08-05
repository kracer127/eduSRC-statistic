# -*- coding:utf-8 -*-
# by:kracer
import re
import requests
import time
from threading import *
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

url0 = "https://src.sjtu.edu.cn/list/?page="

def getData(a):
    with open(r'edusrc.txt', 'a+', encoding='utf-8') as f:
        for page in range((1 + a - 100), (a+1)):
            url = url0 + str(page)
            r = requests.get(url=url)
            r.encoding = r.apparent_encoding
            soup = bs(r.text, 'lxml')
            result = soup.find_all(name='tr', attrs={'class':'row'})
            soup1 = bs(str(result), 'lxml')
            result1 = soup1.find_all(name='a')
            # result2 = soup1.find_all(name='span')  #高危 低危...
            # naem = re.findall(r'([\u4e00-\u9fa5].*)', str(result))
            result_list = [i.string for i in result1]
            for i in range(len(result_list)):
                if(i%2 == 0):
                    text = re.findall(r'(\w.*)', result_list[i])
                    print(text)
                    f.write(str(text[0]) + '\n')
                else:
                    continue
        # print([i.string for i in result1])

def Th(fuc):
    t = []
    for i in range(1, 21):
        Th1 = Thread(target=fuc, args=(100*i,))
        t.append(Th1)
    for i in t:
        i.start()
    for j in t:
        j.join()

def process():
    global edu_name, bug_name
    edu_name, bug_name = [], []
    with open('edusrc.txt', 'r+', encoding='utf-8') as f:
        for i in f.readlines():
            Chakai = i.split('存在')
            edu_name.append(Chakai[0])
            bug_name.append(Chakai[1].strip('\n'))
    with open('edu_name.txt', 'a+', encoding='utf-8') as f1:
        for i in edu_name:
            f1.write(str(i) + '\n')
    with open('bug_name.txt', 'a+', encoding='utf-8') as f2:
        for i in bug_name:
            f2.write(str(i) + '\n')

def Tongji():
    dic_bug = {"SQL": 0, "CSRF": 0, "SSRF": 0, "XSS": 0, "代码执行": 0, "其他": 0, "命令执行": 0, "垂直权限": 0, "弱口令": 0, "敏感信息": 0, "文件上传": 0, "水平权限": 0, "点击劫持": 0}
    count = 0
    name = []
    with open('bug_name.txt', 'r+', encoding='utf-8') as f1:
        datas = f1.readlines()
        print("总条数：" + str(len(datas)))
        for i in datas:
            if 'SQL' in i:
                dic_bug["SQL"] += 1
                count += 1
            elif 'XSS' in i:
                dic_bug["XSS"] += 1
                count += 1
            elif 'SSRF' in i:
                dic_bug["SSRF"] += 1
                count += 1
            elif 'CSRF' in i:
                dic_bug["CSRF"] += 1
                count += 1
            elif '代码执行' in i:
                dic_bug["代码执行"] += 1
                count += 1
            elif '其他' in i:
                dic_bug["其他"] += 1
                count += 1
            elif '命令执行' in i:
                dic_bug["命令执行"] += 1
                count += 1
            elif '垂直权限' in i:
                dic_bug["垂直权限"] += 1
                count += 1
            elif '弱口令' in i:
                dic_bug["弱口令"] += 1
                count += 1
            elif '敏感信息' in i:
                dic_bug["敏感信息"] += 1
                count += 1
            elif '文件上传' in i:
                dic_bug["文件上传"] += 1
                count += 1
            elif '水平权限' in i:
                dic_bug["水平权限"] += 1
                count += 1
            elif '点击劫持' in i:
                dic_bug["点击劫持"] += 1
                count += 1
            else:
                name.append(str(i))
    return dict(sorted(dic_bug.items(), key=lambda k: k[1]))

def Huatu(data, labels, title):
        # 准备数据
        plt.figure(figsize=(15, 15))
        #显示的中文字体设置
        plt.rcParams['font.family'] = 'SimHei'
        # 将排列在第4位的语言(Python)分离出来
        explode = [2.5, 2.5, 0.5, 0.5, 0.5, 0, 0, 0, 0, 0, 0, 0, 0]
        # 使用自定义颜色
        colors = ['navy', 'cyan', 'gold', 'pink', 'magenta', 'darkseagreen', 'm', 'teal', 'deepskyblue', 'tomato', 'green', 'yellowgreen', 'orangered']
        # colors = ['red', 'pink', 'magenta', 'purple', 'orange']
        # 将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆
        plt.axes(aspect='equal')
        # 控制X轴和Y轴的范围(用于控制饼图的圆心、半径)
        plt.xlim(0, 12)
        plt.ylim(0, 12)
        # 不显示边框
        plt.gca().spines['right'].set_color('none')
        plt.gca().spines['top'].set_color('none')
        plt.gca().spines['left'].set_color('none')
        plt.gca().spines['bottom'].set_color('none')
        # 绘制饼图
        plt.pie(x=data,  # 绘制数据
                labels=labels,  # 添加编程语言标签
                explode=explode,  # 突出显示Python
                colors=colors,  # 设置自定义填充色
                autopct='%0.1f%%',  # 设置百分比的格式,保留3位小数
                pctdistance=0.8,  # 设置百分比标签和圆心的距离
                labeldistance=1.1,  # 设置标签和圆心的距离
                startangle=180,  # 设置饼图的初始角度
                center=(6, 5),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
                radius=6,  # 设置饼图的半径(相当于X轴和Y轴的范围)
                counterclock=False,  # 是否为逆时针方向,False表示顺时针方向
                wedgeprops={'linewidth': 1, 'edgecolor': 'aqua'},  # 设置饼图内外边界的属性值
                textprops={'fontsize': 11, 'color': 'black'},  # 设置文本标签的属性值
                frame=1)  # 是否显示饼图的圆圈,1为显示

        # 不显示X轴、Y轴的刻度值
        plt.xticks(())
        plt.yticks(())
        # 显示图形
        # 添加图形标题
        plt.title(title)
        plt.show()

def main():
    data_list, label_list = [], []
    data = Tongji()
    for k, v in data.items():
        data_list.append(k)
        label_list.append(v)
    print()
    Huatu(label_list, data_list, "2020-2021年教育业漏洞排行榜")

if __name__ == "__main__":
    main()