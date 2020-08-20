# -*- coding: utf-8 -*-
import scrapy
from yes24.items import Yes24Item  

class Yes24BestSpider(scrapy.Spider):
    name = 'yes24_best'
    allowed_domains = ['yes24.com/24/Category/BestSeller']
    start_urls = ['http://yes24.com/24/Category/BestSeller/']

    def parse(self, response):
        name_of_books = response.css('#bestList > ol > li > p:nth-child(3)>a::text').getall()
        price_of_books =response.css('#bestList > ol > li > p.price>strong::text').getall()
        if len(name_of_books) == len(price_of_books) : 
            for num, title in enumerate(name_of_books):
                item = Yes24Item()
                item['book_ranking'] = num+1 
                item['book_name'] = title
                item['book_price'] = price_of_books[num].strip().replace('원','').replace(',','')
                yield item



         
