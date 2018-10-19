
# cookie 保存在内存

from urllib import request,parse
from http.cookiejar import CookieJar


# header 作为全局
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def get_opener():
    # 1、自动登录，不用手动拷贝 cookie
    # 1.1 创建一个 cookiejar 对象
    cookiejar = CookieJar()
    # 1.2 使用 cookiejar 创建一个 HTTPCookieProcess 对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的 cookiejar 创建一个 opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    # 1.4 使用 opener 发送登录的请求

    data = {
        'email': '970138074@qq.com',
        'password': 'pythonspider'
    }
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    # request.urlopen(req)
    opener.open(req)


def visit_profile(opener):
    # 访问个人主页
    dapeng_url = 'http://www.renren.com/955947636/profile'

    # 获取个人主页，不要新建 opener
    # 而要使用旧的的 opener,包含了 cookie 信息
    resp = opener.open(dapeng_url)
    with open('renren3.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)