

# 页面等待：
#现在的网页越来越多采用了 Ajax 技术，这样程序便不能确定何时某个元素完全加载出来了。
# 如果实际页面等待时间过长导致某个dom元素还没出来，但是你的代码直接使用了这个WebElement，那么就会抛出NullPointer的异常。
# 为了解决这个问题。所以 Selenium 提供了两种等待方式：一种是隐式等待、一种是显式等待。

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# 因为 expected_conditions 名字太长，所以 as EC ，把 EC 作为别名
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
driver = webdriver.Chrome(executable_path=driver_path)


driver.get("https://www.qq.com/")

# 隐式等待
# driver.implicitly_wait(10) # 等待10秒，再获取 id = Dwyane_Coding 的元素
# driver.find_element_by_id('Dwyane_Coding')


# 显示等待
# 显示等待：显示等待是表明某个条件成立后才执行获取元素的操作。也可以在等待的时候指定一个最大的时间。

# qq中没有 id = 'Dwyane_Coding'，所以会等待10秒再报错
# WebDriverWait(driver,10).until(
#     EC.presence_of_element_located((By.ID,'Dwyane_Coding'))  # 注意：(By.ID,'Dwyane_Coding') 中间不要有空格
# )

# qq.com 有 sougouTxt 这个 id,所以不用等待10s,只要找到这个id的元素，马上返回
element = WebDriverWait(driver,10).until( # until 后面带条件，下面只是条件之一，具体可以 ctr + 鼠标左键查看
    EC.presence_of_element_located((By.ID,'sougouTxt'))  # 注意：(By.ID,'Dwyane_Coding') 中间不要有空格
)
print(element)