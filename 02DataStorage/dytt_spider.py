

from lxml import etree
import requests

# 域名
BASE_DOMAIN = 'http://www.ygdy8.net'
# url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'

HEADERS = {
    'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}



def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)

    # response.text 是系统自己默认判断。但很遗憾判断错误，导致乱码出现。我们可以采取另外方式 response.content。自己指定格式解码
    # print(response.text)
    # print(response.content.decode('gbk'))
    # print(response.content.decode(encoding="gbk", errors="ignore"))
    text = response.content.decode(encoding="gbk", errors="ignore")

    # 通过 xpath 拿到每个电影的详情url
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")

    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls) #这句意思相当于下面一段代码:替换列表中的每一个url
    # def abc(url):
    #     return BASE_DOMAIN+url
    # index = 1
    # for detail_url in detail_urls:
    #     detail_url = abc(detail_url)
    #     detail_urls[index] = detail_url
    #     index+1

    return detail_urls

# 解析详情页面
def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers = HEADERS)
    text = response.content.decode('gbk', errors='ignore')
    html = etree.HTML(text)
    # title = html.xpath("//div[@class='title_all']//font[@color='#07519a']")  # 本行47行，下面已修改

   # 打印出 [<Element font at 0x10cb422c8>, <Element font at 0x10cb42308>]
   #  print(title)

    # 为了显示，我们需要转一下编码
    # for x in title:
    #     print(etree.tostring(x,encoding='utf-8').decode('utf-8'))

     # 我们是为了取得文字，所以修改47行
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']") [0] # 求出共同的顶级容器，方便后面求职
    imgs = zoomE.xpath(".//img/@src") # 求出海报和截图
    cover = imgs[0]
    if len(imgs) > 1:
        screenshot = imgs[1]
        movie['screenshot'] = screenshot
    # print(cover)
    movie['cover'] = cover

    infos = zoomE.xpath(".//text()")

    for index,info in enumerate(infos):
        if info.startswith('◎年　　代'):
            info = info.replace("◎年　　代", "").strip() # strip 去掉空格
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie["country"] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别", "").strip()
            movie["category"] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie["douban_rating"] = info
        elif info.startswith("◎片　　长"):
            info = info.replace("◎片　　长","").strip()
            movie["duration"] = info
        elif info.startswith("◎导　　演"):
            info = info.replace("◎导　　演", "").strip()
            movie["director"] = info
        elif info.startswith("◎主　　演"):
            # info = info.replace("◎主　　演", "").strip()
            # 因为主演有很多个，再加上其在电影天堂中元素的特殊性，需要遍历一遍，在分别求出每一个演员
            actors = []
            for x in range(index+1,len(infos)): # 从演员 infos 开始遍历，求出每一个演员
                actor = infos[x].strip()
                if actor.startswith("◎"): # 也就是到了标签 的 ◎ 就退出
                    break
                actors.append(actor)
            movie['actor'] = actors
        elif info.startswith('◎简　　介 '):

            # info = info.replace('◎简　　介 ',"").strip()
            for x in range(index+1,len(infos)):
                if infos[x].startswith("◎获奖情况"):
                  break
                profile = infos[x].strip()
                movie['profile'] = profile
            # print(movie)
        elif info.startswith('◎获奖情况 '):
            awards = []
            # info = info.replace("◎获奖情况 ", "").strip()
            for x in range(index+1,len(infos)):
                if infos[x].startswith("【下载地址】"):
                    break
                award = infos[x].strip()
                awards.append(award)
            movie['awards'] = awards
            # print(awards)

    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return  movie

def spider():
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    # movies = [] # 前7页的总数据
    # 第一个for循环是为了爬取前7页
    for x in range(1,8):
        url = base_url.format(x) # 求出每一页电影列表的url eg: http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html

        detail_urls = get_detail_urls(url) # 拿到列表中每一步电影的详情页的 url
        movies = []
        # 第二个for循环是为了爬取每一个电影详情页
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
        print('第%d页, %s\n\n' % (x, movies)) # 分别打印前7页的详情页

# 存储写此代码时的html
def store_url():

    url = 'http://www.ygdy8.net/html/gndy/dyzz/20181022/57644.html'
    # return
    resp =  requests.get(url,headers=HEADERS)
    # print(resp.json())

    with open('movie.html','w',encoding='gbk') as fp:
         fp.write(resp.content.decode('gbk', errors='ignore'))
    print("搞定")

if __name__ == '__main__':
    spider()
    # store_url()
