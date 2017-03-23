# python3 phones.py
# Read newBusiness1.py.csv
# Lookup phone numbers on the Internet.
# Write pyhone.py.csv
# From https://docs.python.org/3.6/library/csv.html

__author__ = 'DaleEMoore@gMail.Com'
import csv
import scrapy

class mwSpider(scrapy.Spider):
    name = "mw"
    start_urls = [
        'http://cms.mooreworks.net/cms/11blog.aspx',
    ]
    def parse(selfself, response):
        for mw in response.css('div.quote'):
            yield {
                'text': mw.css('span.text::text').extract_first(),
                'author':mw.css('small.author::text').extract_first(),
                'tags': mw.css('div.tags a.tag::text').extract(),
            }

rowCounter = 0
with open('newBusiness1.py.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    # spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # the_fieldnames = next(spamreader) # read next line so header will be accessed
    # print(the_fieldnames)
    # the_fieldnames = spamreader.next() # read next line so header will be accessed
    # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        rowCounter += 1
        print("Read at row " + str(rowCounter))
        print(str(row))
        print(row["ZipFile"] + row["TxtFile"] + row["DocumentNumber"])
        # TODO; run through https://doc.scrapy.org/en/latest/intro/tutorial.html and learn SCRAPY!
        # dalem@Mercury2:~/PycharmProjects/newBusiness1⟫ scrapy crawl mw -o mw.json
        # below 2, does nothing
        # spider = scrapy.Spider
        # mwSpider(spider)
        # Scrapy has a cloud https://scrapy.org/
        # TODO; Use scrapy or BeautifulSoup to search web. scrapy is powerful framework; BeautifulSoup parses a URL.
        # Use scrapy. Install and configure scrapy.
        # https://doc.scrapy.org/en/latest/intro/examples.html
        # https://github.com/scrapy/quotesbot
        # dalem@QnD:~/PycharmProjects/newBusiness1⟫ scrapy crawl mw --logfile ./scrapy.log
        # Nice scrapy tutorial: https://doc.scrapy.org/en/latest/intro/tutorial.html
        # Selectors: https://doc.scrapy.org/en/latest/topics/selectors.html
        # TODO; use scrapy command line "scrapy crawl mw --logfile ./scrapy.log" to find some stuff in MooreWorks.Net.
        # TODO; use scrapy in parse.py to do the same thing as "scrapy crawl mw --logfile ./scrapy.log".

        # TODO; google lookup phone numbers
        # Google Search BusinessOwner1, PropertyAddress2, PropertyAddressCity, PropertyAddressState, PropertyAddressZip
        # TODO; write this spamreader row and the new information.
        # print(', '.join(row))
        if rowCounter > 10:
            print("Breaking at row " + str(rowCounter))
            break
# import csv
# with open('newBusiness1.py.csv', 'rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print (', '.join(row))
print("Done at row " + str(rowCounter))