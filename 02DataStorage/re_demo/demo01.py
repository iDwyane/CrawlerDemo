

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
text = '1-22'
ret = re.match('[\d\-]+',text)
print(ret.group())
