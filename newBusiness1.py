"""
New businesses come in via ZIP as TXT files and look something like this:

General Information

Document Number:  20140486141 Book Type:  ASSUMED NAMES
Filed Date:  8/14/2014 Filing Time:  2:06:19 PM
Instrument Type:  ABANDONMENT Comment:
# of Pages:  2
Business Owner

FIT THERAPY OF TEXAS OR FIT THERAPY OF TEXAS LLC
 FIT THERAPY OF TEXAS OR FIT THERAPY OF TEXAS LLC

Property Address

Address 1: .
Address 2: 1842 DEER TRAIL
City: FLORESVILLE
State: TX
Zip: 78114-
"""

__author__ = 'dalem'

import os

#Select ZIP file from Downloads
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)
# /home/dalem/Downloads/BEXAR_TXT_08142014.ZIP

#Pull out TXT file(s)
import zipfile
file = zipfile.ZipFile(filename, 'r')
zipMembers = file.infolist()

#Process each TXT file extracting data and exporting into LibreOffice Database.
for member in zipMembers:
    #print member, member.filename, member.orig_filename, member.date_time
    rd = file.read(member,"r")
    #print rd
    ad = rd.splitlines()
    #00 General Information
    #01
    #02 Document Number:  20140486166 Book Type:  ASSUMED NAMES
    #03 Filed Date:  8/14/2014 Filing Time:  4:43 PM
    documentNumber = ad[2][18:29].strip()
    bookType = ad[2][42:].strip()
    fileDate = ad[3][12:22].strip()
    fileTime = ad[3][36:].strip()
    s1 = "{}, {}, {}, {}, {}, {}".format(os.path.basename(filename), member.filename, documentNumber, bookType, fileDate, fileTime)
    #print s1
    #print filename, member.filename, documentNumber, bookType, fileDate, fileTime

    #04 Instrument Type:  UNINCORPORATED Comment:
    #   0123456789.123456789.123456789.123456789.123456789.123456789.
    #05 # of Pages:  2
    #06 Business Owner
    #07
    #08 SW TRAILER RENTALS
    #09  RIVERA, DINAH ANN
    #10 RIVERA, RUDY RAUL
    instrumentType = ad[4][18:31].strip()
    commentAD = ad[4][41:].strip()
    numberOfPages = ad[5][11:].strip()
    businessOwner1 = ad[8].strip()
    businessOwner2 = ad[9].strip()
    businessOwner3 = ad[10].strip()
    s2 = "{}, {}, {}, {}, {}, {}".format(instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3)
    #print s1
    #print instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3

    #11
    #12 Property Address
    #13
    #14 Address 1: .
    #   0123456789.123456789.123456789.123456789.123456789.123456789.
    #15 Address 2: 7407 CANOPUS BOW
    #16 City: SAN ANTONIO
    #17 State: TX
    #18 Zip: 78252-
    propertyAddress1 = ad[14][11:].strip()
    propertyAddress2 = ad[15][11:].strip()
    propertyAddressCity = ad[16][6:].strip()
    propertyAddressState = ad[17][7:].strip()
    propertyAddressZip = ad[18][5:].strip()
    s3 = "{}, {}, {}, {}, {}".format(propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip)
    #print s1
    #print propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip
    # /home/dalem/Downloads/BEXAR_TXT_08142014.ZIP
    print "{}, {}, {}".format(s1, s2, s3)