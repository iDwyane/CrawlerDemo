
# WebElement 类，有很多，可以 ctr + 鼠标左键，进去看一下属性
from selenium import webdriver

driver_path = r'/Users/aaa/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.qq.com')
driver.get('https://www.baidu.com/')
submitBut = driver.find_element_by_id('su')
print(type(submitBut))
print(submitBut.get_attribute("value"))  # get_attribute：这个标签的某个属性的值。
# driver.save_screenshot('qq.png') # 对浏览器上的腾讯进行截图