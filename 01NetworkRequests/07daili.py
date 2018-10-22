
# 使用requests 请求，使用代理

import requests


proxy = {
    'http':'118.190.95.35:9001'
}

response = requests.get("http://httpbin.org/ip",proxies=proxy)
print(response.text)