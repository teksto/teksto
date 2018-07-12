# 采集 http://www.ccamc.co/tangut.php?unicode= 中数据，生成西夏文字典文件。
# 0x17000
# 0x187ff
# 不需要部首部分。

import requests
import json
import csv

# 采集地址 
url= 'http://www.ccamc.co/tangut.php?unicode='

# 采集范围
u= 0x17000
# n= 0x187ff
n= 0x1700f

# 生成文件名
o0= 'tangut.csv'
o1= 'tg.json'
o2= 'tg.yaml'



# 循环测试
for i in range(u,n):
  print (i)