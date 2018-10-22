
# 共用 cookies
import requests

# response = requests.get('http://www.baidu.com/')
# print(response.cookies.get_dict()); # 获取 cookies


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
data = {
    'email': '970138074@qq.com',
    'password': 'pythonspider'
}

login_url = 'http://www.renren.com/PLogin.do'

session = requests.session()

session.post(login_url,data=data,headers=headers)

dapeng_url = 'http://www.renren.com/955947636/profile'

response = session.get(dapeng_url)

with open('dapeng2.html','w',encoding='utf-8') as fp:
    fp.write(response.text)