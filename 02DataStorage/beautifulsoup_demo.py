
from bs4 import BeautifulSoup

html = """
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
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">1359</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=10#a">2</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=20#a">3</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=30#a">4</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=40#a">5</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=50#a">6</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=60#a">7</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=70#a">...</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=1350#a">136</a><a href="position.php?lid=&tid=87&keywords=请输入关键词&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
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
tr = soup.find_all("tr",limit=3)[1]  # limit 最多获取多少个元素  下标【1】 跟 xpath 不同
print(tr)