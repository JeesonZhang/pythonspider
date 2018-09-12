# -*- coding: utf-8 -*-
import scrapy
from firstscrapy.items import FirstscrapyItem
from bs4 import BeautifulSoup
import re


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://www.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # pass
        # 用BeautifulSoup()方法将源码内容生成能用BeautifulSoup解析的lxml格式文件
        BS = BeautifulSoup(response.text, 'lxml')
        # 用find_all()方法找到包含电影的所有标签
        movies = BS.find_all(name='div', attrs={'class': 'item'})
        # 遍历每一个电影信息
        for movie in movies:
            # 实例化一个item对象，用来存放数据
            item = FirstscrapyItem()
            # 提取图片的地址信息
            item['img'] = movie.find(name='img', attrs={'width': '100'}).attrs['src']
            # 提取电影名字信息
            item['name'] = movie.find(name='span', attrs={'class': 'title'}).string
            # 提取电影介绍信息
            # 注意：get_text()能提取包含有内嵌标签的信息
            intro = movie.find(name='p', attrs={'class': ''}).get_text()
            # 用正则提取所有的可见字符
            intro = re.findall('\S', intro, re.S)
            # 将列表转化为字符串
            item['intro'] = ''.join(intro)
            # 提取评价信息
            # 注意：评价信息分别在在多个<span>里面，所以用findall()方法
            star = movie.find(name='div', attrs={'class': 'star'}).find_all(name='span')
            # 获取评分
            item['score'] = star[1].string
            # 获取评价人数
            item['fans_num'] = star[3].string
            # 获取引语
            item['quote'] = movie.find(name='span', attrs={'class': 'inq'}).string
            # 生成一条item数据给自动传给pipeline处理
            yield item
