# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class FirstscrapyPipeline(object):
    def process_item(self, item, spider):
        try:
            # 连接到数据库
            db = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456xun',
                                 db='csdn',
                                 charset='utf8mb4')
        except:
            print('连接失败')


        # 创建操作游标
        cursor = db.cursor()
        # 编写sql插入语句
        sql_insert = '''INSERT INTO top(img, name, intro, score, fans_num, quote) VALUES (%s, %s, %s, %s, %s, %s)'''


        # 用try尝试执行插入
        try:
            cursor.execute(sql_insert, (item['img'], item['name'], item['intro'], item['score'], item['fans_num'], item['quote']))
            db.commit()
        except:
            print('保存失败')
        return item
