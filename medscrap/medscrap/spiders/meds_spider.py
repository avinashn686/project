import scrapy
# from ..items import MedscrapItem

class MedSpider(scrapy.Spider):
    name = 'med'
    start_urls = [
        'https://healthapps.dhss.mo.gov/showmeltc/default.aspx',
    ]
    def parse(self, response):
    	# items=MedscrapItem()
    	# drop_box=response.css('select#ContentPlaceHolder1_ddlCounty > option :: attr(value)').extract()
    	# yield drop_box
    	for drop in response.css('select#ContentPlaceHolder1_ddlCounty > option :: attr(value)').extract():
    		yield scrapy.FormRequest('https://healthapps.dhss.mo.gov/showmeltc/default.aspx',formdata = {'drop':response.css('select#ContentPlaceHolder1_ddlCounty > option[selected] ::attr(value)').extract()})
    # def parse_result(self, response):
    # 	yield{}