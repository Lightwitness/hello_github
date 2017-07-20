#!/usr/bin/env python
# encoding: utf-8
"""
@version: python2.7
@author: Lightwitness
@contact: 498969498@qq.com
@software: PyCharm
@file: zhilian.py
@time: 2017/7/20 21:57
"""
import requests
from lxml import etree
import json

def run():
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' \
          'jl=%E6%B7%B1%E5%9C%B3&kw=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&p=1'

    user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

    headers = {'User-Agent' : user_agent}

    req = requests.get(url , headers = headers)

    # with open("./zhilian.html" , "a") as f:
    #     f.write(req.text.encode("UTF-8"))
    #     print "chenggong"
    selector = etree.HTML(req.text)
    selectname = selector.xpath('//*[@id="newlist_list_content_table"]/table[@class = "newlist"]')[0]
    jobs = selectname.xpath('//td[@class = "gsmc"]/a/text()')
    dict={}

    for job in jobs :
        dict[u"公司名称"] = job
        write_fp(dict)


def write_fp(item):
    jStr = json.dumps(item, ensure_ascii=False)
    str = jStr.encode('Utf-8')

    with open("./zhilian.json" , "a") as f:
        f.write(str + '\n')
        print "成功"





if __name__ == "__main__":
    run()