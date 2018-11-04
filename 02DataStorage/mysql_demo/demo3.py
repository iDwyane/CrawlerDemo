

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='z1234567',
                       database='pymysql_demo',port=3306)

cursor = conn.cursor()

# sql = """
#     select username,age from user where id = 4
# """
#
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)

####### fectchone #######
# sql = """
#     select * from user
# """
#
# cursor.execute(sql)
# while True:
#     result = cursor.fetchone()
#     if result:
#         print(result)
#     else:
#         break
# conn.close()

####### fetchall #######
# sql = """
#     select * from user
# """
#
# cursor.execute(sql)
# results = cursor.fetchall()
# for result in results:
#     print(result)
#
# conn.close()


####### fectchone #######
sql = """
    select * from user
"""

cursor.execute(sql)
results = cursor.fetchmany(2)
for result in results:
    print(result)

conn.close()