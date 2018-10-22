

import  requests

# 1.将目标网址上的页面抓取下来

headers = {
    'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'Referer':
}

url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
response = requests.get(url, headers=headers)
print(response.text)