

import re

# 1、匹配某个字符串
# text = 'hello'
# ret = re.match('he',text)
# print(ret.group())

# 2、点：匹配任意的字符
# text = '+hello'
# ret = re.match('.',text) # 只匹配一个任意字符，但不可以匹配换行符号
# print(ret.group())

# 3、\d:匹配任意的数字（0-9）
# text = "8"
# ret = re.match('\d', text)
# print(ret.group())

# 4、\D：匹配任意的非数字
# text = "-"
# ret = re.match('\D', text)
# print(ret.group())

# 5、 \s: 匹配空白符(\n \t \r 空格)
# text = "\t"
# ret = re.match('\s',text)
# print(ret.group())

# 6、 \w: 匹配的是 a-z,A-Z,数字和下划线
# text = "b"
# ret = re.match('\w',text)
# print(ret.group())

# 7、 \W：与 \w 相反
# text = "+"
# ret = re.match('\W',text)
# print(ret.group())


# 8、 []组合的方式，只要满足中括号中的字符，就可以匹配
# text = '1-22'
# ret = re.match('[\d\-]+',text)
# print(ret.group())


# 9、*：可以匹配0或者多个字符
# text = "3a1bcd"
# ret = re.match("\d*", text)
# print(ret.group())

# 10、+：可以匹配1或者多个字符
# text = "13ab6cd"
# ret = re.match("\d+", text)
# print(ret.group())

# 11、?:匹配一个或0个，要么没有，要么只有一个
# text = "234"
# ret = re.match("\w?", text)
# print(ret.group())

# 12、?:匹配一个或0个，要么没有，要么只有一个
# text = "234"
# ret = re.match("\W?", text)
# print(ret.group())

# 13、{m}:匹配m个字符
# text = "234ab"
# ret = re.match("\d{2}", text)
# print(ret.group())

# 14、{m,n}:匹配m-n个字符。在这中间的字符都可以匹配到
# text = "2d34absds124"
# ret = re.match("\w{1,4}", text)
# print(ret.group())


######### 小案例 #########

# 15、验证手机号码
# text = "18820898963"
# ret = re.match("1[34578]\d{9}", text)
# print(ret.group())

# 16、验证邮箱
# text = "dwyane@163.com"
# ret = re.match("\w+@[a-z0-9]+\.[a-z]+",text)
# print(ret.group())

# 17、验证url
# text = "https://www.jianshu.com/u/bb2db3428fff"
# ret = re.match("(http|https|ftp)://[^\s]+",text)   # [^\s] 非空白符
# print(ret.group())


# 18、验证身份证
# text = "44010319900307883X"
# ret = re.match("\d{17}[\dxX]",text)
# print(ret.group())

# 19、验证用户名(用户名长度为6-20位之间,大小写字母或者数字均可)
text = "abCDf1245"
ret = re.match("^[A-Za-z0-9]{6,20}$",text)
print(ret.group())

# 19、^ (脱字号) 在macth函数中可以省略，效果一样，都是以什么开头
# text = "adX"
# ret = re.match("^a",text)
# print(ret.group())

# 20、search
# text = "adX"
# ret = re.search("d",text)
# print(ret.group())

# 21、 $ 以什么结尾
# text = "xxx@163.com"
# ret = re.match("\w+@163.com$",text)
# print(ret.group())

# 22、 |：匹配多个表达式或者字符串：
# text = "hello|world|love"
# ret = re.search('love',text)
# print(ret.group())

# 23、 贪婪模式
# text = "0123456"
# ret = re.match('\d+',text)
# print(ret.group())

# 24、可以改成非贪婪模式，那么就只会匹配到0
# text = "0123456"
# ret = re.match('\d+?',text)
# print(ret.group())


# 匹配0-100之间的数字：
# text = '99'
# ret = re.match('[1-9]?\d$|100$',text)  # 记得有个 $ 结尾
# print(ret.group())
