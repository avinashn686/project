# import scrapy
from scrapy.http import FormRequest
# from ..items import MedscrapItem
class MedScrap(scrapy.Spider):
    name = 'med'
    start_urls = ['https://healthapps.dhss.mo.gov/showmeltc/default.aspx']
    nexturl='https://healthapps.dhss.mo.gov/showmeltc/default.aspx'
    # download_delay = 1.5


    def parse(self, response):
        # response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
        drop_list=response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
        for l in drop_list:
            # print (l)
            yield scrapy.FormRequest.from_response(response, formid="ContentPlaceHolder1_pnlSearchandResults",
                formdata={'ctl00$ContentPlaceHolder1$ddlCounty': l},
                callback=self.parse_button
                )
            
            

    def parse_button(self, response):
        # items=MedscrapItem()
        rows=response.css('table#ContentPlaceHolder1_gvSearchResults tr')
        # for row in rows:
            next_page=row.css('td').css('a::attr(href)').extract_first()
            # print(next_page)
        
            response.follow('row.css("td").css("a::attr(href)").extract_first()')
            # print (response.body)
            # allitem=response.css("div.form-group").extract()
            # # print (allitem)
            # for det in allitem:

                
            #     faculty_name = response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_FacilityName_0::text').extract_first()
            #     administrator= response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_Label2_0::text').extract_first()
            #     address = response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblAddress_0::text').extract_first()
            #     address2 = response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblCityStateZip_0::text').extract_first()
            #     phonenumber= response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblPhoneNumber_0::text').extract_first()
            #     operator= response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lbloperator_0::text').extract_first()
            #     total_lisence_beds = response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblTotalLicensedBeds_0::text').extract_first()
            #     medicare = response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicareBeds_0::text').extract_first()
            #     medicaid = response.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicaidBeds_0::text').extract_first()
            #     items['faculty_name']= faculty_name
            #     items['administrator']= administrator
            #     items['address']= address
            #     items['address2']= address2
            #     items['phonenumber']= phonenumber
            #     items['operator']= operator
            #     items['total_lisence_beds']= total_lisence_beds
            #     items['medicare']= medicare
            #     items['medicaid']= medicaid
            #     yield items
                
                # print(faculty_name)
                # filename = 'newfile.json' 
                # with open(filename, 'ab') as f:
                #     f.write(faculty_name)
                #     f.write(administrator)
                #     f.write(address)
                #     f.write(address2)
                #     f.write(phonenumber)
                #     f.write(operator)
                #     f.write(total_lisence_beds)
                #     f.write(medicare)
                #     f.write(medicaid)
                # self.log('Saved file %s' % filename)
        # table=response.css('table#ContentPlaceHolder1_gvSearchResults ')
        # print (table)

        # g=response.xpath('//*[@id="ContentPlaceHolder1_gvSearchResults" ]/table/tbody/tr').extract()
        # print (g)

    # def output(self, response):
    #     allitem=response.css('div.row')
    #     for det in allitem:
    #         faculty_name=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_FacilityName_0::text').extract()
    #         administrator=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_Label2_0::text').extract()
    #         address=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblAddress_0::text').extract()
    #         address2=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblCityStateZip_0::text').extract()
    #         phonenumber=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblPhoneNumber_0::text').extract()
    #         operator=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lbloperator_0::text').extract()
    #         total_lisence_beds=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblTotalLicensedBeds_0::text').extract()
    #         medicare=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicareBeds_0::text').extract()
    #         medicaid=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicaidBeds_0::text').extract()

    #         filename = 'newfile.json' 
    #         with open(filename, 'ab') as f:
    #             f.write(faculty_name,administrator,address,address2,phonenumber,operator,total_lisence_beds,medicare,medicaid)
    #         self.log('Saved file %s' % filename)














        # response.css('input#ContentPlaceHolder1_btnShowMeResults')
        # response.css('input#ContentPlaceHolder1_btnShowMeResults').get()
        
        # 'https://healthapps.dhss.mo.gov/showmeltc/default.aspx'

        # page = response.css('div.body').extract()
        # print (page)
        # filename = 'newfile.html' 
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

















































































































































# import scrapy
# from scrapy.http import FormRequest
# class MedScrap(scrapy.Spider):
#     name = 'med'
#     start_urls = ['https://healthapps.dhss.mo.gov/showmeltc/default.aspx']
#     nexturl='https://healthapps.dhss.mo.gov/showmeltc/default.aspx'
#     # download_delay = 1.5


#     def parse(self, response):
#         # response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
#         # drop_list=response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
#         drop_list=response.xpath('//*[@id="ContentPlaceHolder1_ddlCounty"]/option').extract()
#         for l in drop_list:
            
#             yield scrapy.FormRequest.from_response(
#                 response, formxpath="//div[@id='ContentPlaceHolder1_pnlSearchandResults']",
#                 url=self.nexturl,
#                 formdata={
                    
#                     '__EVENTTARGET': l ,
#                     'ContentPlaceHolder1_ddlCounty': response.css(
#                         'select#ContentPlaceHolder1_ddlCounty > option[selected] ::attr(value)'
#                     ).extract_first(),

#                     '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first(),
                    
#                 },

#                 callback=self.parse_button

                
#             )
            

#     def parse_button(self, response):
#         
#         g=response.xpath('//*[@id="ContentPlaceHolder1_gvSearchResults" ]/table/tbody/tr').extract()
#         print (g)
#         for row in response.xpath('//*[@id="ContentPlaceHolder1_gvSearchResults" ]/table/tbody/tr').extract():

#             next_page=response.css(rows.css('td')[0].css(a)).extract_first()
#             yield response.follow(next_page, callback=self.output)


#     def output(self,response):
#         allitem=response.css('div.row')
        # for det in allitem:
        #     faculty_name=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_FacilityName_0::text').extract()
        #     administrator=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_Label2_0::text').extract()
        #     address=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblAddress_0::text').extract()
        #     address2=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblCityStateZip_0::text').extract()
        #     phonenumber=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblPhoneNumber_0::text').extract()
        #     operator=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lbloperator_0::text').extract()
        #     total_lisence_beds=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblTotalLicensedBeds_0::text').extract()
        #     medicare=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicareBeds_0::text').extract()
        #     medicaid=det.css('span#ContentPlaceHolder1_gvFacilitySearchDetail_lblMedicaidBeds_0::text').extract()

        #     filename = 'newfile.json' 
        #     with open(filename, 'ab') as f:
        #         f.write(faculty_name,administrator,address,address2,phonenumber,operator,total_lisence_beds,medicare,medicaid)
        #     self.log('Saved file %s' % filename)
#         # for row in response.xpath('//*[@class="table table-striped"]//tbody/tr'):
# #             yield {
# #                 'first' : row.xpath('td[1]//text()').extract_first(),
# #                 'last': row.xpath('td[2]//text()').extract_first(),
# #                 'handle' : row.xpath('td[3]//text()').extract_first(),
# #             }
# # next_page=response.css('li.next a::attr(href)').get()
# #         if next_page is not None:
# #             yield response.follow(next_page, callback = self.parse)


        
#         # 'https://healthapps.dhss.mo.gov/showmeltc/default.aspx'
#         # rows=response.css('table#ContentPlaceHolder1_gvSearchResults').get()
#         # for row in rows:
#         #     print (rows.css('td')[0].css(a))
#         # page = response.css('table')
#         # print (page)
#         # filename = 'newfile.html' 
#         # with open(filename, 'wb') as f:
#         #     f.write(page)
#         # self.log('Saved file %s' % filename)

