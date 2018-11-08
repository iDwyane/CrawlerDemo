

# selenium 入门
# selenium 发现之初并不是用来爬虫，而来拿来自动化测试，省去人工点击的麻烦

from selenium import webdriver
import time

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://baidu.com')  # 会打开谷歌浏览器，访问 qq.com

time.sleep(5)

# driver.close() # 关闭

driver.quit() # 退出整个浏览器