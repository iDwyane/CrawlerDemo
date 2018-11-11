
# 打开多窗口和切换窗口

from selenium import webdriver


driver_path = r'/Users/aaa/Downloads/chromedriver'  # 加 r 表示原生字符串
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.baidu.com/")

# 执行javascript代码
driver.execute_script("window.open('https://www.qq.com/')")
print(driver.window_handles)

# 切换到 第二个url
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
print(driver.page_source)

# 虽然窗口中切换了新页面，但是 driver 还没有切换
# 如果想代码中切换到新页面，应该使用 driver.switch_to.window 来切换到指定的窗口
# driver.window_handles 是一个 list （数组），它按照打开页面的顺序来存储窗口的句柄