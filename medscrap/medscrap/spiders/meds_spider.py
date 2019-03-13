import scrapy
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
        for row in rows:
            next_page=row.css('td').css('a::attr(href)').extract_first()
            
            d.append(next_page)
            
        for i in d:
            yield scrapy.FormRequest.from_response(response,
                formdata={'__EVENTTARGET': i
                },
                callback=self.output
            )
    def output(self, response):
        
        filename = 'newfile.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


    #     allitem=response.css("div.form-group").extract()
    #     for allitems in allitem:        
    #         print (allitem)
            # filename = 'newfile.html' 
            # with open(filename, 'wb') as f:
            #     f.write(allitem)
            # self.log('Saved file %s' % filename)

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














   















































































































































