
# selenium 定位元素的方法详解

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://baidu.com')  # 会打开谷歌浏览器，访问 qq.com

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_class_name('s_ipt')
# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input") # CSS 选择器
# inputTag = driver.find_elements_by_css_selector(".quickdelete-wrap > input")[0]
# 也可以把 by 放进 括号中
inputTag = driver.find_elements(By.CSS_SELECTOR,".quickdelete-wrap > input")[0]

print(inputTag)
inputTag.send_keys('python')

# 有些时候不得不使用driver
# 解析网页内容，推荐使用lxml,把网页源代码给lxml解析， lxml底层是C语言，解析效率会更高
# 如果是想要对元素的进行一些操作，比如给一个文本框输入值，或者是点击某个按钮，那么必须使用 selenium 给我们提供的查找元素的方法。

