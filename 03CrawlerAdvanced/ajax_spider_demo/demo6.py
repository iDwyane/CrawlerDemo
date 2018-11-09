
# Cookie 操作
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com')

# 遍历所有 cookie
# for cookie in driver.get_cookies():
    # print(cookie)

# 返回一个name为了的cookie,当然，没有找到则返回 "None"
print(driver.get_cookie('PSTM'))

# driver.delete_cookie('PSTM')

driver.delete_all_cookies() # 删除所有cookie  ctr + shift + del 进入内容设置，可查看当前浏览器 cookie

print(driver.get_cookie('PSTM'))