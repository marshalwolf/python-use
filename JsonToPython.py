#coding=utf-8
#将JSON格式转换成Python对象

import json
jsonData = '{"a" :1, "b" :2, "c" :3, "d" :4 }'
#json.dumps() 将Python对象转换成JSON对象
#json.loads() 将JSON对象转换成Python对象
input = json.loads(jsonData)
print (input)