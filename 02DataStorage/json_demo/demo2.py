

# loads跟文件无关 loads()方法是将字符串json转换为字典 load则与文件有关

import json

# json_str = '[{"username":"张三", "age":18, "country":"China"},{"username":"李思", "age":20, "country":"China"}]'
#
# persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
#     print(person)


with open('person.json', 'r', encoding="utf-8") as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons:
        print(person)