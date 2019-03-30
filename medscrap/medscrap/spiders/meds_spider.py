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
        n=len(drop_list)
        for l in range(1,n,1):
        	
            
            yield scrapy.FormRequest.from_response(response, formid="ContentPlaceHolder1_pnlSearchandResults",
                formdata={'ctl00$ContentPlaceHolder1$ddlCounty': drop_list[l]},
                callback=self.parse_button
                )
            
            

    def parse_button(self, response):
        
        rows=response.css('table#ContentPlaceHolder1_gvSearchResults tr')
        c=0
        d=[]
        
        for row in rows[1:]:
            next_page=row.css('td').css('a::attr(href)').extract_first()
                        d.append(next_page)
        
        for i in range(0,len(d),1):
            
            r=''
            j='ctl00$ContentPlaceHolder1$gvSearchResults'
            k='select$'
            r=k+str(i)

            yield scrapy.FormRequest.from_response(response, formid="ContentPlaceHolder1_PnlsrchResults",
                formdata={
                '__EVENTTARGET':j ,
                '__EVENTARGUMENT': r,
                
                
                
                },
            callback=self.output

            )
            

    
    def output(self, response):
        
        filename = 'newfile4.html' 
        with open(filename, 'ab') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


    










   















































































































































