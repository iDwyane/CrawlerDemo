
from urllib import request
# 大鹏主页 http://www.renren.com/955947636/profile
# 登录url 'http://www.renren.com/PLogin.do'
# 不使用 cookie 请求大鹏主页
dapeng_url = 'http://www.renren.com/955947636/profile'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie':'anonymid=jne9tzin-of6dv8; depovince=GUZ; _r01_=1; JSESSIONID=abcGGKb0dAK7_bONIggAw; ick_login=9b89b2c7-d8f6-4989-8564-9e935ea40feb; t=405579761a14245476e400f45c7c75413; societyguester=405579761a14245476e400f45c7c75413; id=968394463; xnsid=79e5a383; jebe_key=f190a9a7-6293-4eb6-8abb-bf5f5483d028%7Ce49410ed7b1c7842306bd5bf08c436b6%7C1539848169151%7C1%7C1539848171703; wp_fold=0; XNESSESSIONID=ca5a1f22f843; jebecookies=bf0ccad2-85d3-4b67-a485-4614baf5f4e9|||||'
}

req = request.Request(url = dapeng_url, headers = headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren.html', 'w') as fp:
    # write 函数必须写入一个str数据类型
    # resp.read()读出来的是一个bytes数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))  # 去到的是一个登录页面