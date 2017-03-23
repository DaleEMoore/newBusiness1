
# From: https://scrapy.org/

# Was https://blog.scrapinghub.com/
# src view-source:https://blog.scrapinghub.com/

# Now  http://cms.mooreworks.net/cms/11blog.aspx
# src view-source:http://cms.mooreworks.net/cms/11blog.aspx

# dalem@Mercury2:~/PycharmProjects/newBusiness1⟫ scrapy runspider mwspider.py -o mwspider.json
# Look in mwspider.json for output data.

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://cms.mooreworks.net/cms/11blog.aspx']

    def parse(self, response):
        for title in response.css('art-Logo'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
