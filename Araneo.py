# coding= utf-8
import os
import csv
import yaml
import json
import time
from lxml import etree
from urllib import request

# 抓取ccamc.tangut部分
# sub= 94208
sub= 94229
# sup= 100351
sup= 94235

# 时间戳
tm= time.time()

# 数组列表转字串
def ts(arr):
  return ','.join(arr)

# CSV写入
def rec(data):
  with open('datumoj.csv', 'a', encoding='utf-8', newline='') as f:
    csv.writer(f).writerow(data)

# YAML写入
def rey(data):
  print(data)

# JSON生成
def rej(data):
  print(data)

# korpo
def sp(id):
  ur= 'http://www.ccamc.co/tangut.php?unicode=' +id
  pg= request.urlopen(ur).read()
  da= etree.HTML(pg)

  # 目标数据
  o1= 'Tg' +id
  s1= ts(da.xpath('//*[p="序號"]/p[2]/text()'))
  m0= ts(da.xpath('//code/preceding-sibling::text()'))
  m1= m0.replace(u'\xa0',u'')
  m10= ts(da.xpath('//p[code]/following-sibling::p[1]/text()'))
  m11= m10.replace(u'詳細解釋請參考。',u'')
  # m12= ts(da.xpath('//p[code]/following-sibling::p[2]/text()'))
  m2= ts(da.xpath('//code/text()'))
  r1= ts(da.xpath('//*[p="音"]/p[3]/text()'))
  r2= ts(da.xpath('//*[p="擬音"]/p/a/text()'))
  r3= ts(da.xpath('//p[b="英文釋義"]/following-sibling::p[1]/text()'))
  c1= ts(da.xpath('//*[p="四角號碼"]/p/a/text()'))
  c2= ts(da.xpath('//*[p="Unicode"]/p[2]/text()'))
  c3= ts(da.xpath('//*[p="Unicode名稱"]/p[2]/text()'))

  # 拼接JSON
  ouj={
    o1:{
      "ser": s1,
      "mea": [[m1,m11], m2],
      "rel": [r1, r2, r3],
      "rime":[],
      "code":[c1, c2, c3]
    },
  }
  # 拼接YAML
  ouy= ''
  # 拼接数组
  our= [o1, s1, m1, m11, m2, r1, r2, r3, c1, c2, c3]

  # 输出
  return our
  # return ouj
  # return ouy

# 进击的八脚战士
# rec(['tangut', tm])
rec(['tangut', 20181115,1])
for i in range(sub,sup):
  hh= hex(i)[2:]
  rec(sp(hh))
  # rey(sp(hh))