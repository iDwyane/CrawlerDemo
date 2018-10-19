
# 爬取拉钩招聘信息

from urllib import request,parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context




# url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
# resp = request.urlopen('https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=')
# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

# 拉钩广州python
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'



headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?px=default&city=%E5%B9%BF%E5%B7%9E'
}

data = {
    'first' : 'true',
    'pn': 1,
    'kd': 'python'
}




# 'POST'是大写
req = request.Request(url, headers = headers, data = parse.urlencode(data).encode('utf-8'), method = 'POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))

