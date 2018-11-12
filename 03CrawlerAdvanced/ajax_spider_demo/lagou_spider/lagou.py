

import requests
from lxml import etree
import time
import re

headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Cookie':'_ga=GA1.2.1316637701.1539793416; user_trace_token=20181018002334-feb64c31-d228-11e8-bcf4-525400f775ce; LGUID=20181018002334-feb64ee5-d228-11e8-bcf4-525400f775ce; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAAIAACBIE683CF5BC65AED1FF3E2D09D130587B9; _gat=1; LGSID=20181112230518-5df59ddf-e68c-11e8-889a-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539793416,1540134945,1542035124; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1542035162; LGRID=20181112230555-741f5160-e68c-11e8-9c38-525400f775ce; SEARCH_ID=45e3e9e43a6841cbba7d70cd4cd010be',
        'Origin':'https://www.lagou.com'
    }

# 在不知道是缺少什么而影响爬取不了，可以选择发送整个浏览器的headers
def request_list_url():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'

    data = {
        'first':'false',
        'pn':1,
        'kd':'python'
    }

    for x in range(1,14):
        data["pn"]:x
        response = requests.post(url,headers=headers,data=data)
        #json 方法：如果返回来的是json数据，那么这个方法会自动的load成字典

        # print(response.json())
        # print('\n'*2)
        result = response.json()
        positions = result['content']['positionResult']['result']

        for position in positions:
            positionId = position['positionId']  # 职位的id
            # 详情页的变化就是职位的id,所以id 跟 url 有关
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId
            parse_postion_detail(position_url)
            break
        # time.sleep(1)
        break

def parse_postion_detail(url):
    response = requests.get(url, headers = headers)
    text = response.text # 拿到详情页的html 源码
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    print(position_name)

    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()  # .strip() 去掉空格
    print(salary)

    city = job_request_spans[1].xpath(".//text()")[0].strip()
    # 把 / 和 空格符去掉
    city = re.sub(r"[\s/]","",city)  # \s匹配的是空白字符
    print(city)

    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]","",work_years)  # \s匹配的是空白字符
    print(work_years)

    education = job_request_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r"[\s/]","",education)
    print(education)

def main():
    request_list_url()


if __name__ == '__main__':
    main()