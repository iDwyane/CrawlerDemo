
# 使用 requests 访问拉钩数据，并且以 json 格式打印

import requests

data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}

headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

response = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false',data=data,headers=headers)

print(response.json())
with open('lagou2.html','w',encoding='utf-8') as fp:
    fp.write(response.json)

