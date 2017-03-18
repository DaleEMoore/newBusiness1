# python3 phones.py
# Read newBusiness1.py.csv
# Lookup phone numbers on the Internet.
# Write pyhone.py.csv
# From https://docs.python.org/3.6/library/csv.html

__author__ = 'DaleEMoore@gMail.Com'
import csv
with open('newBusiness1.py.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    #spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    #the_fieldnames = next(spamreader) # read next line so header will be accessed
    #print(the_fieldnames)
    #the_fieldnames = spamreader.next() # read next line so header will be accessed
    #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(str(row))
        print(row["ZipFile"] + row["TxtFile"] + row["DocumentNumber"])
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
        #print(', '.join(row))
#import csv
#with open('newBusiness1.py.csv', 'rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print (', '.join(row))