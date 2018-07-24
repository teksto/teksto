# 采集 http://www.ccamc.co/tangut.php?unicode= 中数据，生成西夏文字典文件。
# 0x17000
# 0x187ff
# 不需要部首部分。

import csv
import json
import requests
from bs4 import BeautifulSoup

# 采集地址 
url= 'http://www.ccamc.co/tangut.php?unicode='

# 采集范围
u= 0x17000
# n= 0x187ff
n= 0x1700f