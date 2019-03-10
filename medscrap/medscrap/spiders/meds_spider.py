import scrapy
class MedScrap(scrapy.Spider):
    name = 'med'
    start_urls = ['https://healthapps.dhss.mo.gov/showmeltc/default.aspx']
    nexturl='https://healthapps.dhss.mo.gov/showmeltc/default.aspx'
    # download_delay = 1.5


    def parse(self, response):
       ponse.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
        drop_list=response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
        for l in drop_list:
            
            yield scrapy.FormRequest(
                url=self.nexturl,
                formdata={
                    
                    '__EVENTTARGET': l ,
                    'ContentPlaceHolder1_ddlCounty': response.css(
                        'select#ContentPlaceHolder1_ddlCounty > option[selected] ::attr(value)'
                    ).extract_first(),

                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                    
                },
                callback=self.parse_button

                
            )
            

    def parse_button(self, response):
        # response.css('input#ContentPlaceHolder1_btnShowMeResults')
        response.css('input#ContentPlaceHolder1_btnShowMeResults').get()
        
        # 'https://healthapps.dhss.mo.gov/showmeltc/default.aspx'

        page = response.css('div.tbody').extract()
        print (page)
        filename = 'newfile.html' 
        with open(filename, 'wb') as f:
            f.write(page)
        self.log('Saved file %s' % filename)

