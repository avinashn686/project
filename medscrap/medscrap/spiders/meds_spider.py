import scrapy
class MedScrap(scrapy.Spider):
    name = 'med'
    start_urls = ['https://healthapps.dhss.mo.gov/showmeltc/default.aspx']
    # download_delay = 1.5

    def parse(self, response):
        dropdown=response.css('select#ContentPlaceHolder1_ddlCounty > option ::attr(value)').extract()
        for drop in dropdown:
            yield scrapy.FormRequest(
                'https://healthapps.dhss.mo.gov/showmeltc/default.aspx',
                formdata={
                    # 'author': author,
                    'ContentPlaceHolder1_ddlCounty' : response.css(
                        'select#ContentPlaceHolder1_ddlCounty > option[selected] ::attr(value)').extract_first(),
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                # callback=self.parse_tags
            )

    # def parse_tags(self, response):
    #     for tag in response.css('select#tag > option ::attr(value)').extract():
    #         yield scrapy.FormRequest(
    #             'http://quotes.toscrape.com/filter.aspx',
    #             formdata={
    #                 'author': response.css(
    #                     'select#author > option[selected] ::attr(value)'
    #                 ).extract_first(),
    #                 'tag': tag,
    #                 '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
    #             },
    #             callback=self.parse_results,
    #         )

    # def parse_results(self, response):
    #     for quote in response.css("div.quote"):
    #         yield {
    #             'quote': quote.css('span.content ::text').extract_first(),
    #             'author': quote.css('span.author ::text').extract_first(),
    #             'tag': quote.css('span.tag ::text').extract_first(),
    #         }