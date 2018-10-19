
# 代理的使用

from urllib import request

# 代理的原理
# 在请求目的网站前，先请求代理服务器，然后让代理服务器去请求目的网站，代理服务器拿到目的网站的数据后，再转发给我们的代理。
# 就算代理地址被封，仍旧可以切换其他地址，继续请求
# 没有使用代理
# url = 'http://httpbin.org/ip'
#
# resp = request.urlopen(url)
#
# print(resp.read())


# 使用代理

url = 'http://httpbin.org/ip'

# 1、使用 proxyHandler,传入代理构建一个 handler
handler = request.ProxyHandler({"http":"125.70.13.77:8080"})
# 2、使用上面创建的 handler 构建一个 opener
opener = request.build_opener(handler)
# 3、使用 opener 去发送一个请求
resp = opener.open(url)
print(resp.read())