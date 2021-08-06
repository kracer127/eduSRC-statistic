# -*- coding:utf-8 -*-
# by:kracer
import re
import requests
import time
from threading import *
from multiprocessing import Process
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

url0 = "https://src.sjtu.edu.cn/list/?page="
submitter_index_dic, edu_index_dic = {}, {}
datas = []  #承载爬虫获取的数据(列表形式）
bug_name = ["SQL", "CSRF", "SSRF", "XSS", "代码执行", "其他", "命令执行", "垂直权限", "弱口令", "敏感信息", "文件上传", "水平权限", "点击劫持"]
lock = Lock()
#爬取平台网站数据函数
def getData(a, num):
    with open(r'edusrc.txt', 'w+', encoding='utf-8') as f:
        for page in range((num + a - 300), (a+1)):
            url = url0 + str(page)
            r = requests.get(url=url)
            r.encoding = r.apparent_encoding
            soup = bs(r.text, 'lxml')
            result = soup.find_all(name='tr', attrs={'class':'row'})
            soup1 = bs(str(result), 'lxml')
            result0 = soup1.find_all(name='a')  #初始的a标签数据
            result1 = [i.string for i in result0]
            result1_new = []  #正则获取学校漏洞名称
            for i in range(len(result1)):
                if(i%2 == 0):
                    text = re.findall(r'(\w.*)', result1[i])
                    result1_new.append(text[0])
                else:
                    continue
            result2 = re.findall(r'<a.+>(.*)</a>', str(result0)) #正则匹配用户名
            result3 = soup1.find_all(name='span')  #高危 低危...
            result3 = [i.string for i in result3]
            for i in range(len(result1_new)): #写进txt文件
                f.write(str(result1_new[i]) + '\t' + str(result2[i]) + '\t' + str(result3[i]) + '\n')

#设置多线程爬取函数
def Th(fuc, num):
    t = []
    for i in range(1, 21):
        Th1 = Thread(target=fuc, args=(100*i, num,))
        t.append(Th1)
    for i in t:
        i.start()
    for j in t:
        j.join()

#设置多进程爬取函数
def Pr(fuc, num):
    t = []
    for i in range(1, 11):
        Pr1 = Process(target=fuc, args=(300*i, num,))
        t.append(Pr1)
    for i in t:
        i.start()
    for j in t:
        j.join()

#对爬取所得数据进行处理
def process():
    global datas, edu_index_list, submitter_index_dic
    times = 0
    edu_dic, submitter_dic = {}, {}
    with open('edusrc.txt', 'r+', encoding='utf-8') as f:
        for i in f.readlines():
            i.rstrip('\n')
            lis = i.split('\t')
            if len(lis) == 3: #处理特殊数据报错情况
                datas.append(i.split('\t'))
                submitter_dic.setdefault(datas[times][1], {}) #初始化外层字典的key值
                submitter_dic[datas[times][1]].setdefault(datas[times][2].rstrip('\n'), 0) #初始化内层字典的key值，并且赋值value=0
                submitter_dic[datas[times][1]][datas[times][2].rstrip('\n')] += 1 #内层字典的value值 +1
                try:
                    name = re.findall(r'(.*["学"|"院"|"厅"|"部"|"会"|"司"|"局"|"区"|"T"|"馆"|"他"|"心"])', datas[times][0])[0]  #正则匹配学校名
                except Exception as e:
                    print(datas[times][0])
                edu_dic.setdefault(name, {})
                edu_dic[name].setdefault(datas[times][2].rstrip('\n'), 0)
                edu_dic[name][datas[times][2].rstrip('\n')] += 1
                times += 1
            else:
                continue
    for k_1, v_1 in edu_dic.items(): #计算每个大学的漏洞总数
        v_1["总数"] = 0
        for k_2 in v_1.keys():
            if "总数" == k_2:
                continue
            else:
                v_1["总数"] += v_1[k_2]
    edu_dic_new = sorted(edu_dic, key=lambda x: edu_dic[x]["总数"], reverse=True)
    for k_3, v_3 in submitter_dic.items(): #计算每个submitter的漏洞总数
        v_3["总数"] = 0
        for k_4 in v_3.keys():
            if "总数" == k_4:
                continue
            else:
                v_3["总数"] += v_3[k_4]
    edu_dic_new = sorted(edu_dic, key=lambda x: edu_dic[x]["总数"], reverse=True)
    submitter_dic_new = sorted(submitter_dic, key=lambda x: submitter_dic[x]["总数"], reverse=True)
    for edu in edu_dic_new:  #根据漏洞总数进行二重字典排序
        edu_index_dic[edu] = edu_dic[edu]
    for submitter in submitter_dic_new:
        submitter_index_dic[submitter] = submitter_dic[submitter]
    return datas, submitter_index_dic, edu_index_dic

#对用户输入查询年份的预处理函数
def processYear(year):
    if year == "2021":
        print("正在爬取{0}年数据......".format(year))
        Pr(getData, 1)
        print("数据采集完毕, 请选择下一步操作......")
        processFinish()
    elif year == "2020":
        print("正在爬取{0}年数据......".format(year))
        Pr(getData, 3000)
        print("数据采集完毕, 请选择下一步操作......")
        processFinish()
    elif year == "2019":
        print("正在爬取{0}年数据......".format(year))
        Pr(getData, 5000)
        print("数据采集完毕, 请选择下一步操作......")
        processFinish()
    else:
        print("正在爬取{0}年数据......".format(year))
        Pr(getData, 7000)
        print("数据采集完毕, 请选择下一步操作......")
        processFinish()

#数据采集完成后的分析操作预处理函数
def processFinish():
    print("正在处理数据并进行分析可视化......")
    process()
    print("对edu大学|提交者进行排名分析并写进txt文件......")
    edu_submitter_rank(datas, edu_index_dic, submitter_index_dic)
    print("数据写入文件完成.......")
    print("处理完毕，统计各类型漏洞数据......")
    Tongji_bug(datas)
    print("统计完毕，进行漏洞类型画饼图可视化......")
    Huatu(dic_bug)

#对edu大学|提交者进行排名分析, 写进txt文件
def edu_submitter_rank(datas, edu_index_dic, submitter_index_dic):
    for bug in bug_name:
        for index_edu in edu_index_dic.keys():
            edu_index_dic[index_edu].setdefault(bug, 0)
        for index_submitter in submitter_index_dic.keys():
            submitter_index_dic[index_submitter].setdefault(bug, 0)
    for i in datas:
        name = re.findall(r'(.*["学"|"院"|"厅"|"部"|"会"|"司"|"局"|"区"|"T"|"馆"|"他"|"心"])', i[0])[0]  # 正则匹配学校名
        submitter = i[1]
        for j in bug_name:
            if j in i[0]:
                edu_index_dic[name][j] += 1
                submitter_index_dic[submitter][j] += 1
    with open('edu_rank.txt', 'w+', encoding='utf-8') as f, open('submitter_rank.txt', 'w+', encoding='utf-8') as f1:
        for i in edu_index_dic.keys():
            f.write(str(i) + '\n')
            for j in edu_index_dic[i]:
                f.write('\t' + str(j) + ":" + str(edu_index_dic[i][j]) + "个" + '\n')
        for k in submitter_index_dic.keys():
            f1.write(str(k) + '\n')
            for l in submitter_index_dic[k]:
                f1.write('\t' + str(l) + ":" + str(submitter_index_dic[k][l]) + "个" + '\n')

#对各类型漏洞数据进行统计画饼图可视化
def Tongji_bug(datas):
    global dic_bug
    dic_bug = {"SQL": 0, "CSRF": 0, "SSRF": 0, "XSS": 0, "代码执行": 0, "其他": 0, "命令执行": 0, "垂直权限": 0, "弱口令": 0, "敏感信息": 0, "文件上传": 0, "水平权限": 0, "点击劫持": 0}
    for i in datas:
        for j in bug_name:
            if j in i[0]:
                dic_bug[j] += 1
    dic_bug = dict(sorted(dic_bug.items(), key=lambda k: k[1], reverse=True))

#对统计好的漏洞类型数据进行可视化(饼图）
def Huatu(data):
        # 准备数据
        data_list, label_list = [], []
        for k, v in data.items():
            data_list.append(v)
            label_list.append(k)
        title = "2020-2021年教育业漏洞排行榜"
        plt.figure(figsize=(15, 15))
        #显示的中文字体设置
        plt.rcParams['font.family'] = 'SimHei'
        # 将排列在第4位的语言(Python)分离出来
        explode = [0, 0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        # 使用自定义颜色
        colors = ['silver', 'cyan', 'khaki', 'pink', 'magenta', 'darkseagreen', 'm', 'teal', 'skyblue', 'tomato', 'green', 'yellowgreen', 'lime']
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
        plt.pie(x=data_list,  # 绘制数据
                labels=label_list,  # 添加编程语言标签
                explode=explode,  # 突出显示Python
                colors=colors,  # 设置自定义填充色
                autopct='%0.1f%%',  # 设置百分比的格式,保留3位小数
                pctdistance=0.8,  # 设置百分比标签和圆心的距离
                labeldistance=1.1,  # 设置标签和圆心的距离
                startangle=180,  # 设置饼图的初始角度
                center=(6, 5),  # 设置饼图的圆心(相当于X轴和Y轴的范围)
                radius=6,  # 设置饼图的半径(相当于X轴和Y轴的范围)
                counterclock=False,  # 是否为逆时针方向,False表示顺时针方向
                wedgeprops={'linewidth': 1, 'edgecolor': 'red'},  # 设置饼图内外边界的属性值
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
    userChooes = input("是否需要进行数据爬取(y|n)：")
    if userChooes == "y":
        chooesYear = input("请输入要爬取的年份：")
        processYear(chooesYear)
        process()
    elif userChooes == "n":
        processFinish()
    else:
        print("错误！请输入'Y'或者'n'")


if __name__ == "__main__":
    main()