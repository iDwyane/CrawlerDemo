
# 利用 xpath 寻找相关信息

from lxml import etree


parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html',parser=parser)


# 1.获取所有tr标签
# trs = html.xpath("//tr")
# for tr in trs:
#     # print(tr)
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))


# 2.获取第2个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 3.获取所有class等于even的标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 4.获取所有a标签的href属性
# aList = html.xpath("//a/@href")
# for a in aList:
#     print(a)


# 5.获取所有的职位信息（纯文本）
trs = html.xpath("//tr[position()>1]")
positions = []
for tr in trs:
    # 在某个标签下，再执行xpath函数，获取整个标签下的子孙函数，价格 . 相当在当前元素下
    href = tr.xpath(".//a/@href") # "//a" 相当于在整个文档寻找，而不是只在tr下寻找，解决办法是".//a"
    fullurl = 'http://hr.tencent.com/' + href[0]
    title = tr.xpath(".//a/text()")
    title2 = tr.xpath(".//td//text()")[0]
    category = tr.xpath(".//td//text()")[1]  # 等于  category = tr.xpath(".//td[2]//text()")[0]
    category2 = tr.xpath(".//td[2]//text()")[0]
    num = tr.xpath(".//td//text()")[2]
    address = tr.xpath(".//td//text()")[3]
    pubtime = tr.xpath(".//td//text()")[4]

    position =  {
        'url':fullurl,
        'title':category,
        'category':category,
        'nums':num,
        'address':pubtime
    }
    positions.append(position)
    print(position)

    # print(fullurl)
    # print(title)
    # print(title2)
    # print(category2)
    # print(num)
    # print(address)
    # print(pubtime)
    break