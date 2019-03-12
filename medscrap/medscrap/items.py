# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MedscrapItem(scrapy.Item):
    # define the fields for your item here like:
    faculty_name = scrapy.Field()
    administrator=scrapy.Field()
    address=scrapy.Field()
    address2=scrapy.Field()
    phonenumber=scrapy.Field()
    operator=scrapy.Field()
    total_lisence_beds=scrapy.Field()
    medicare=scrapy.Field()
    medicaid=scrapy.Field()
  
