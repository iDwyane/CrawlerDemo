
import  requests
from bs4 import BeautifulSoup
from pyecharts import Bar
ALL_DATA = []

def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    # html5lib 容错性更强
    soup = BeautifulSoup(text, 'html5lib') # 因为港澳台的html格式不规范，所以使用容错率高的html5lib
    # soup = BeautifulSoup(text,'lxml')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table') # 每一个省/直辖市 一个 table
    for table in tables:
        trs = table.find_all('tr')[2:] # 从2开始 每个城市每一个 tr

        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            # print(tds)
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]  # 生成器转成列表，然后取第0个
            temperature_td = tds[-2] # 倒数第二个
            min_temp = list(temperature_td.stripped_strings)[0]
            ALL_DATA.append({'city':city,'min_temp':int(min_temp)})
            # print({'city':city,'min_temp':int(min_temp)})
            # print('='*30)




def main():
    # url = 'http://www.weather.com.cn/textFC/db.shtml'
    # url =  'http://www.weather.com.cn/textFC/hb.shtml'
    # url = 'http://www.weather.com.cn/textFC/hn.shtml'
    # url = 'http://www.weather.com.cn/textFC/xb.shtml'
    # url = 'http://www.weather.com.cn/textFC/xn.shtml'
    # url = 'http://www.weather.com.cn/textFC/gat.shtml'

    urls = {
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    }
    for url in urls:
        parse_page(url)

    # 分析数据
    # 根据最低气温排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    data = ALL_DATA[0:10] # 前十个低温的城市
    cities = list(map(lambda x: x['city'], data))
    temps = list(map(lambda x: x['min_temp'], data))
    chart = Bar("中国天气最低气温排行榜")
    chart.add('',cities,temps)
    chart.render('temperature.html')

if __name__ == '__main__':
    main()