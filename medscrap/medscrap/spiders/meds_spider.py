import scrapy
# from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
# from ..items import MedscrapItem
class MedScrap(scrapy.Spider):
    name = 'med'
    start_urls = ['https://healthapps.dhss.mo.gov/showmeltc/default.aspx']
    nexturl='https://healthapps.dhss.mo.gov/showmeltc/default.aspx'
    # download_delay = 1.5


    def parse(self, response):
        
        drop_list=response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
        for l in drop_list:
            
            yield scrapy.FormRequest.from_response(response, formid="ContentPlaceHolder1_pnlSearchandResults",
                formdata={'ctl00$ContentPlaceHolder1$ddlCounty': l},
                callback=self.parse_button
                )
            
            

    def parse_button(self, response):
        
        rows=response.css('table#ContentPlaceHolder1_gvSearchResults tr')
        c=0
        d=[]
        
        for row in rows[1:]:
            next_page=row.css('td').css('a::attr(href)').extract_first()
            #printing extracted links
            print (next_page)
            d.append(next_page)
        
            # for i in range(len(d)):
            # # print(i)
            #     j='ctl00$ContentPlaceHolder1$gvSearchResults'
            #     yield scrapy.FormRequest.from_response(response, 
            #         formdata={'__EVENTTARGET' : j,
            #         '__EVENTARGUMENT': 'select$%s' +str(i),
            #     # formdata={'select':i,
                
                
            #         },
            #     callback=self.output

                # )
            

    
    # def output(self, response):
        
    #     filename = 'newfile.html' 
    #     with open(filename, 'ab') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)


    










   















































































































































