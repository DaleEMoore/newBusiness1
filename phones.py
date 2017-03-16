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
        # TODO; google lookup phone numbers
        # TODO; write this spamreader row and the new information.
        #print(', '.join(row))
#import csv
#with open('newBusiness1.py.csv', 'rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print (', '.join(row))