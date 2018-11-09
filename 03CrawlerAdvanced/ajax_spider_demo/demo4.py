

# 常见的表单元素： input type = 'text/password/email/number' 文本框      input type = 'submit'则是按钮
# button input[type=['submit]
# checkbox: input='checkbox'
# select: 下拉列表

# 操作输入框
# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.by import By
#
# driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://baidu.com')  # 会打开谷歌浏览器
#
#
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
#
# time.sleep(3)
#
# inputTag.clear() # 清除

# 操作 checkbox 对豆瓣网登录底下的 记住我  打钩
# from selenium import webdriver
# import time
#
# from selenium.webdriver.common.by import By
#
# driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('https://douban.com')  # 会打开谷歌浏览器
#
#
# inputTag = driver.find_element_by_id('form_remember')
# time.sleep(3)
# inputTag.click() # 选中 / 取消训中



# 携程
# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import Select
#
# from selenium.webdriver.common.by import By
#
# driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
#
# driver = webdriver.Chrome(executable_path=driver_path)
#
# driver.get('http://www.ctrip.com/?allianceid=1381&sid=1068414')  # 会打开谷歌浏览器
#
#
# inputTag = Select(driver.find_element_by_id('searchHotelLevelSelect'))
# time.sleep(3)
# inputTag.select_by_index(1)
# # 根据值选择
# # inputTag.select_by_value("2")
# # 根据可视的文本选择
# inputTag.select_by_visible_text("四星级/高档")
# # 取消选中所有选项
# # inputTag.deselect_all()


# 百度网输入值并点击搜索
from selenium import  webdriver
driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('Dwyane_Coding')

submitTag = driver.find_element_by_id('su')
submitTag.click() # 点击搜索框
