# -*- coding: utf-8 -*-
import scrapy


class MwSpider(scrapy.Spider):
    name = "mw"
    allowed_domains = ["mooreworks.net"]
    start_urls = ['http://cms.mooreworks.net/cms/11blog.aspx']
    # http://cms.mooreworks.net/cms/11blog.aspx
    #start_urls = ['http://mooreworks.net/']

    def parse(self, response):
        # From: https://github.com/scrapy/quotesbot/blob/master/quotesbot/spiders/toscrape-xpath.py
        # TODO; look at http://stackoverflow.com/questions/25826823/scrapy-python-xpath-how-to-extract-data-from-within-data
        # http://pythonscraping.com/blog/xpath-and-scrapy
        # https://blog.scrapinghub.com/2014/07/17/xpath-tips-from-the-web-scraping-trenches/
        # https://doc.scrapy.org/en/0.10.3/topics/selectors.html

        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        pass
