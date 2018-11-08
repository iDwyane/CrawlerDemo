

# 常见的表单元素： input type = 'text/password/email/number' 文本框      input type = 'submit'则是按钮
# button input[type=['submit]
# checkbox: input='checkbox'
# select: 下拉列表


from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://baidu.com')  # 会打开谷歌浏览器，访问 qq.com


inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')