
# selenium 入门
# selenium 发明之初并不是用来爬虫，而来拿来自动化测试，省去人工点击的麻烦

from selenium import webdriver

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.qq.com')  # 会打开谷歌浏览器，访问 qq.com

print(driver.page_source)