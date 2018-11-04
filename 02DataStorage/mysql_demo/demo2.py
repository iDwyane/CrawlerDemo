

import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost',user = 'root', password='z1234567',
                       database='pymysql_demo', port=3306)
# 创建一个游标
cursor = conn.cursor()

# 执行语句
# sql = """
#     insert into user(id,username,age,password) values (2, 'bbb', 20, '111111')
# """
#
# cursor.execute(sql)
#
# conn.commit()


sql = """
    insert into user(id,username,age,password) values (null, %s, %s, %s)
"""

username = 'spider'
age = 23
password = '123000'
cursor.execute(sql, (username, age, password))

conn.commit()
# 关闭
conn.close()