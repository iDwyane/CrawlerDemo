

import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost',user = 'root', password='z1234567',
                       database='pymysql_demo', port=3306)
# 创建一个游标
cursor = conn.cursor()

# 执行语句
cursor.execute("select 1")

result = cursor.fetchone()
print(result)

# 关闭
conn.close()



