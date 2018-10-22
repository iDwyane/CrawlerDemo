
# 学习lxml框架

from lxml import etree

text = '''
<html>
<head>
	<!-- meta -->
	<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="renderer" content="webkit">
<meta property="qc:admins" content="23635710066417756375" />
<meta name="baidu-site-verification" content="QIQ6KC1oZ6" />

<meta content="互联网招聘,找工作,招聘网,人才网" name="keywords">

<meta content="拉勾网是权威的互联网行业招聘平台。提供全国真实可靠的互联网招聘信息。工资不面议。找工作、要招聘、搜人才就来拉勾网。互联网行业找工作首选拉勾网" name="description">

<title>拉勾网-专业的互联网招聘平台_找工作_招聘_人才网_求职</title>

<link rel="Shortcut Icon" href="//www.lgstatic.com/www/static/common/static/favicon_faed927.ico"></head>
'''


def parse_text():
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


def parse_file():

    # 通过文件读取，遇到不规范的的格式，请指定解析器
    parser = etree.HTMLParser(encoding='utf-8')

    htmlElement = etree.parse('tencent.html',parser=parser)

    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_text()