
# selenium 行为链

from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com')

inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag,'Dwyane_Coding')
actions.move_to_element(submitTag)

actions.click(submitTag)
actions.perform()

# click_and_hold(element)：点击但不松开鼠标。
# context_click(element)：右键点击。
# double_click(element)：双击。 更多方法请参考：http: // selenium - python.readthedocs.io / api.html
