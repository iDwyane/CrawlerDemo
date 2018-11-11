
# 使用代理 ip
from selenium import webdriver

driver_path = r'/Users/aaa/Downloads/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://112.98.126.100:33421")

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

# 访问该网址可以得到代理后的ip
driver.get("http://httpbin.org/ip")