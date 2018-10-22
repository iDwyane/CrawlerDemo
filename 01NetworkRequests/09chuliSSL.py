
# 处理不信任的SSL证书

import requests

# 如果证书不被通过，报错，可以添加 verify=False
resp = requests.get('http://www.12306.cn/mormhweb/',verify=False)
print(resp.content.decode('utf-8'))
