# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class MedscrapPipeline(object):
    
    def __init__(self):
    	self.create_connection()
    	self.create_table()
    def create_connection(self):
    	self.conn= sqlite3.connect("details.db")
    	self.curr= self.conn.cursor()
    def create_table(self):
    	self.curr.execute("""drop table if exists details_tb""")
    	self.curr.execute("""create table details_tb(faculty_name text, administrator text, address text, address2 text, phonenumber text, operator text, total_lisence_beds text, medicare text, medicaid text)""")
    def process_item(self, item, spider):
    	self.store_db(item)
    	print ("pipeline :" + item['faculty_name'][0])
    	return item
    def store_db(self,item):
    	self.curr.execute("""insert into details_tb values(?,?,?,?,?,?,?,?,?)""",(
    	item['faculty_name'][0],
    	item['administrator'][0],
    	item['address'][0],
    	item['address2'][0],
    	item['phonenumber'][0],
    	item['operator'][0],
    	item['total_lisence_beds'][0],
    	item['medicare'][0],
    	item['medicaid'][0],


    		))
    	self.conn.commit()
