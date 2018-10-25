
# 使用requests 请求，使用代理

import requests


proxy = {
    'http':'42.231.251.104:80'
}

response = requests.get("http://httpbin.org/ip",proxies=proxy)
response2 = requests.get('https://mp.weixin.qq.com/s/Fk3dxhXnAo0hsYuiOu6fmg',proxies=proxy)
print(response.text)
print("="*30)
print(response2.text)