# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
 

class Yes24Pipeline(object):
    def process_item(self, item, spider):
        if int(item['book_ranking']) <= 30 :
            return item
        else : 
            raise DropItem("drop item lanking is more than 30 ")
        
        

        
