
from bs4 import BeautifulSoup

html = """
    			<div class="right pl9" id="topshares">
    				<div class="shares">
    					<span class="left">分享到：</span>
		    			<!--<a href="javascript:;" onclick="shareto('qqt','top');" id="qqt" title="分享到腾讯微博">分享到腾讯微博</a>-->
		    			<a href="javascript:;" onclick="shareto('qzone','top');" id="qzone" title="分享到QQ空间">分享到QQ空间</a>
		    			<!--<a href="javascript:;" onclick="shareto('pengyou','top');" id="pengyou" title="分享到腾讯朋友">分享到腾讯朋友</a>-->
		    			<a href="javascript:;"  onclick="shareto('sinat','top');"id="sinat" title="分享到新浪微博">分享到新浪微博</a>
		    			<!--<a href="javascript:;"  onclick="shareto('renren','top');"id="renren" title="分享到人人网">分享到人人网</a>-->
		    			<!--<a href="javascript:;"  onclick="shareto('kaixin001','top');"id="kaixin" title="分享到开心网">分享到开心网</a>-->
		    			<div class="clr"></div>
    				</div>
    				<!--<a href="javascript:;">分享</a>-->
    			</div>
    			<!--<div class="right pl9">-->
    				<!--<a href="http://t.qq.com/QQjobs" id="tqq" target="_blank">收听腾讯招聘</a>-->
    			<!--</div>-->
    			<div class="right pr9">
    			
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44968&keywords=&tid=87&lid=0">PCG01-QQ后台推荐算法工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>湛江</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44970&keywords=&tid=87&lid=0">PCG01-QQ后台高级数据分析工程师</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-22</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44971&keywords=&tid=87&lid=0">23674-腾讯新闻大数据分析工程师（北京）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>北京</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44962&keywords=&tid=87&lid=0">PCG11-web前端工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44964&keywords=&tid=87&lid=0">TEG05-高级数据挖掘工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44969&keywords=&tid=87&lid=0">PCG01-QQ后台大数据开发工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44954&keywords=&tid=87&lid=0">22989-腾讯云大数据产品高级咨询顾问（深圳北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44955&keywords=&tid=87&lid=0">22989-腾讯云大数据产品高级咨询顾问（深圳北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44960&keywords=&tid=87&lid=0">18425-国际支付业务高级java研发工程师 (深圳)</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-10-22</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44963&keywords=&tid=87&lid=0">TME-腾讯音乐音频检索算法工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-10-22</td>
		    	</tr>
		    	
		    </table>
"""


# 创建  Beautiful Soup 对象
# 使用lxml来进行解析
soup = BeautifulSoup(html,"lxml") # 指定一个解析器，也可以不指定，它自己使用自带的

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.a)
# print(soup.a)


# 1、获取所有 tr 标签
trs = soup.find_all('tr')
for tr in trs:
    # print(tr)
    # print("="*30)
    # print(type(tr))  # 打印 " <class 'bs4.element.Tag'> " 得出是一个Tag的类型
    break

# 获取第2个tr标签
# tr = soup.find_all("tr",limit=3)[1]  # limit 最多获取多少个元素  下标【1】 跟 xpath 不同
# print(tr)

# 获取所有class等于 even 的tr标签
# trs = soup.find_all('tr', class_='even')  # class_ 为了区分python 的关键字 class
# trs = soup.find_all('tr', attrs = {"class":"even"})
# for tr in trs:
#     print(tr)
#     print("="*30)

# 4、将所有id 等于 test,class 也等于test 的a标签
# aList = soup.find_all('a', id='test',class_='test')
# aList = soup.find_all('a', attrs={"id":"test","class":"test"})
# for a in aList:
#     print(a)

# 5、获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
#     # 1、通过下表操作的方式
#     # href = a['href']
#     # print(href)
#     # 2、通过attrs属性的方式
#     href = a.attrs['href']
#     print(href)

# 6、获取所有的职位信息
trs = soup.find_all('tr')[1:] # 第 0 个tr标签无效，所以从1开始
for tr in trs:
#     tds = tr.find_all('td')
#     title = tds[0] # 获取第0个td
#     print(title.string)
#     category = tds[1].string
#     print(category)
#     nums = tds[2].string
#     print(nums)
#     city = tds[3].string
#     print(city)

    # infos = tr.strings
    # for info in infos:
    #     print(info)
    #     print("="*20)

    # 去掉多余空格
    infos = list(tr.stripped_strings)
    # print(infos)






# tr3 = soup.find_all('tr')[1]
# text = tr3.get_text()
# print(text)


soup = BeautifulSoup(html,'lxml')
div = soup.find('div')
print(type(div.children))  # children 是迭代器 list_iterator
print(type(div.contents)) # contents 是列表 list