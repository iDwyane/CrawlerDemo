

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='z1234567',
                       database='pymysql_demo',port=3306)
cursor = conn.cursor()


##### 删除 #####
# sql = """
#     delete from user where id=1
# """
#
# cursor.execute(sql)
#
# # 插入、删除、更新都需要 commit操作
# conn.commit()
# conn.close()



##### 更新 #####

sql = """
    update user set username='aaa' where id=2
"""


cursor.execute(sql)

conn.commit()

conn.close()

