<h1 align="center" >eduSRC-statistic</h1>

<h3 align="center" >善于总结，方能突破</h3>

<p align="center">
    <a href="https://github.com/kracer127/eduSRC-statistic"><img alt="eduSRC-statistic" src="https://visitor-badge.glitch.me/badge?page_id=kracer127.eduSRC-statistic"></a>
    <a href="https://github.com/kracer127/eduSRC-statistic"><img alt="eduSRC-statistic" src="https://img.shields.io/github/stars/kracer127/eduSRC-statistic.svg"></a>
    <a href="https://github.com/kracer127/eduSRC-statistic/releases"><img alt="eduSRC-statistic" src="https://img.shields.io/github/release/kracer127/eduSRC-statistic.svg"></a>
</p>


## 🏝 0x01 介绍
作者：kracer

定位：研究eduSRC网站提交的漏洞数据，对往年所提交的漏洞的进行总结分类

语言：python3开发

功能：多线程收集[教育行业漏洞报告平台](https://src.sjtu.edu.cn/)所提交漏洞数据，并对数据进行整理分析，得出往年各类型漏洞提交的频率饼图及漏洞排名，方便新手入手和确定批量刷洞方向。



## 🎸0x02 安装使用

1、所需库安装

```python
pip3 install requirements.txt
```

2、使用

```python
开启：python eduSRC.py
输入：	input 》是否需要进行数据爬取(y|n)：：eg.（y|n）
输入： input 》请输入要爬取的年份：eg.（2021|2020|2019...）
```

3、说明

```python
文件:edusrc.txt --- 根据年份进行爬取得到的漏洞数据，每条形如：广东省教育厅存在文件上传漏洞	小远	高危
文件：edu_rank.txt --- 该年份下大学漏洞总数的排名及具体漏洞类型分类。
文件：submitter_rank.txt --- 该年份下漏洞提交者的提交总数排名及所提交漏洞类型统计。
另外说明：现存的这三个文件为爬取的2021年数据。
```



## 💡0x03 效果展示
1、2020-2021年提交漏洞的统计饼图：<img src="imgs\image-20210805102136882.png" alt="image-20210805102136882" style="zoom:80%;" />

2、2020-2021年各大学校漏洞统计：

```
年份漏洞总条数：30000

上海交通大学:786个漏洞
江苏省教育厅:496个漏洞
四川省教育厅:430个漏洞
安徽省教育厅:398个漏洞
同济大学:372个漏洞
浙江省教育厅:359个漏洞
山东省教育厅:347个漏洞
浙江大学:332个漏洞
河南省教育厅:307个漏洞
福建省教育厅:304个漏洞			
河北省教育厅:277个漏洞
广东省教育厅:275个漏洞
华东师范大学:261个漏洞
兰州大学:251个漏洞
清华大学:247个漏洞
陕西省教育厅:230个漏洞
电子科技大学:225个漏洞
北京市教育委员会:218个漏洞
广西壮族自治区教育厅:208个漏洞
上海市教育委员会:195个漏洞
湖南省教育厅:186个漏洞
江西省教育厅:159个漏洞
四川大学:156个漏洞
武汉大学:153个漏洞
重庆市教育委员会:149个漏洞
湖北省教育厅:148个漏洞
南开大学:145个漏洞
中国科学技术大学:140个漏洞
华东理工大学:138个漏洞
贵州省教育厅:137个漏洞
云南省教育厅:133个漏洞
甘肃省教育厅:130个漏洞
山西省教育厅:130个漏洞
辽宁省教育厅:127个漏洞
山东大学:121个漏洞
福州大学:113个漏洞
山东理工大学:113个漏洞
......
```

3、2020-2021年学校漏洞排行榜：

```
上海交通大学
	低危:147个
	中危:147个
	高危:67个
	严重:23个
	总数:384个
	SQL:42个
	CSRF:4个
	SSRF:4个
	XSS:17个
	代码执行:13个
	其他:0个
	命令执行:6个
	垂直权限:21个
	弱口令:145个
	敏感信息:100个
	文件上传:21个
	水平权限:11个
	点击劫持:0个
江苏省教育厅
	高危:25个
	低危:59个
	中危:37个
	严重:6个
	总数:127个
	SQL:18个
	CSRF:0个
	SSRF:0个
	XSS:0个
	代码执行:4个
	其他:0个
	命令执行:4个
	垂直权限:1个
	弱口令:37个
	敏感信息:50个
	文件上传:13个
	水平权限:0个
	点击劫持:0个
同济大学
	低危:47个
	中危:62个
	高危:13个
	严重:1个
	总数:123个
	SQL:17个
	CSRF:0个
	SSRF:0个
	XSS:6个
	代码执行:0个
	其他:0个
	命令执行:7个
	垂直权限:4个
	弱口令:43个
	敏感信息:37个
	文件上传:5个
	水平权限:4个
	点击劫持:0个
华东师范大学
	中危:49个
	高危:20个
	低危:49个
	严重:3个
	总数:121个
	SQL:29个
	CSRF:0个
	SSRF:2个
	XSS:10个
	代码执行:0个
	其他:0个
	命令执行:6个
	垂直权限:4个
	弱口令:28个
	敏感信息:32个
	文件上传:3个
	水平权限:7个
	点击劫持:0个
	......
```

4、2020-2021年大佬提交漏洞排行榜：

```
姜洪杰
	中危:252个
	低危:1565个
	高危:47个
	严重:10个
	总数:1874个
	SQL:7个
	CSRF:0个
	SSRF:0个
	XSS:2个
	代码执行:3个
	其他:69个
	命令执行:5个
	垂直权限:0个
	弱口令:876个
	敏感信息:911个
	文件上传:1个
	水平权限:0个
	点击劫持:0个
远海
	高危:191个
	低危:20个
	中危:207个
	严重:1个
	总数:419个
	SQL:167个
	CSRF:0个
	SSRF:0个
	XSS:0个
	代码执行:0个
	其他:32个
	命令执行:1个
	垂直权限:30个
	弱口令:34个
	敏感信息:6个
	文件上传:140个
	水平权限:8个
	点击劫持:1个
鲁中代表
	高危:12个
	中危:35个
	低危:372个
	总数:419个
	SQL:7个
	CSRF:0个
	SSRF:0个
	XSS:0个
	代码执行:6个
	其他:11个
	命令执行:2个
	垂直权限:1个
	弱口令:52个
	敏感信息:337个
	文件上传:3个
	水平权限:0个
	点击劫持:0个
flank
	高危:36个
	低危:123个
	中危:101个
	严重:11个
	总数:271个
	SQL:11个
	CSRF:0个
	SSRF:0个
	XSS:11个
	代码执行:23个
	其他:101个
	命令执行:10个
	垂直权限:2个
	弱口令:86个
	敏感信息:28个
	文件上传:2个
	水平权限:1个
	点击劫持:0个
教主assassin
	中危:99个
	低危:93个
	高危:33个
	严重:7个
	总数:232个
	SQL:15个
	CSRF:0个
	SSRF:1个
	XSS:10个
	代码执行:2个
	其他:56个
	命令执行:15个
	垂直权限:15个
	弱口令:64个
	敏感信息:33个
	文件上传:8个
	水平权限:13个
	点击劫持:0个
	......
```

