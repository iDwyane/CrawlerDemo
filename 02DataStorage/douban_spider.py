

import requests
from lxml import etree

# 1.将目标网址上的页面抓取下来

headers = {
    'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'Referer':
}

url = 'https://movie.douban.com/cinema/nowplaying/guangzhou/'
response = requests.get(url, headers=headers)
text = response.text
# 2.将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
lis = ul.xpath("./li")
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    release = li.xpath("@data-release")[0]
    # alt = li.xpath(".//img/@alt")[0]
    # print(thumbnail)
    # print(title)
    # print(alt)


    movies = []
    movie = {
        'title':title,
        'score':score,
        "duration":duration,
        "director":director,
        "actors":actors,
        "thumbnail":thumbnail,
        "release":release
    }

    movies.append(movie)

    print(movies)