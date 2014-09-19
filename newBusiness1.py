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

# Format error in BEXAR_TXT_09052014.ZIP 00000069.TXT
#   Same error in BEXAR_TXT_09102014.zip 00000055.TXT
"""
General Information

Document Number:  20140487023 Book Type:  ASSUMED NAMES
Filed Date:  9/5/2014 Filing Time:  1:29:54 PM
Instrument Type:  VOID Comment:  VOIDED
# of Pages:  1
Business Owner

VOID, VOID VOID
 VOID, VOID VOID
"""
# Since it's the last .TXT file in the .ZIP, I'll process each of the two .ZIP files one at a time.
# Same problem in BEXAR_TXT_09082014.ZIP last two .TXT files 82 and 83. Maybe the last ones are
# where the VOIDs go.

__author__ = 'dalem'

import os

#Select ZIP file from Downloads
from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# keep the last folder used for the next run. (Maybe http://goo.gl/2lkJV0) or default to ~/Downloads.
# default to files named *.ZIP. (Lots of info here http://tkinter.unpythonic.net/wiki/tkFileDialog)
# Cool: http://nullege.com/codes/show/src@k@a@kamaelia-HEAD@Code@Python@Kamaelia@Kamaelia@Apps@Whiteboard@Decks.py/123/Tkinter.Tk.withdraw
# TODO; persist theDir from previous run? Read my question here
# http://programmers.stackexchange.com/questions/253527/where-to-save-something-between-invocations?noredirect=1#comment510007_253527
# appdirs (https://pypi.python.org/pypi/appdirs/1.4.0) might be best part of figuring out where to save the data.
theDir = "~/Downloads"
filenames = askopenfilename(multiple=1,filetypes=[("Zip Archives",("*.zip", "*.ZIP"))],initialdir=theDir,title="Businesses ZIP with TXTs")
#filename = askopenfilename(filetypes=[("Zip Archives",("*.zip", "*.ZIP"))],initialdir=theDir,title="Businesses ZIP with TXTs")
#filename = askopenfilename(filetypes=[("Zip Archives",("*.zip", "*.ZIP"))],initialdir=theDir,title="Load Slide Deck",parent=root)
#filetypes = [
#("Image Files", ("*.jpg", "*.gif")),
#("JPEG",'*.jpg'),
#("GIF",'*.gif'),
#('All','*')
#]
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)
# /home/dalem/Downloads/BEXAR_TXT_08142014.ZIP
if filenames=="":
    exit()

# put the data into a LibreOffice DB; or import .csv.
fileOutName = os.path.basename(__file__) + ".csv"
print fileOutName
fileOut = open(fileOutName, 'w')

# put column headings out first.
s4 = "ZipFile"
s4 += ",TxtFile"
s4 += ",DocumentNumber"
s4 += ",BookType"
s4 += ",FileDate"
s4 += ",FileTime"
s4 += ",InstrumentType"
s4 += ",Comment"
s4 += ",NumberOfPages"
s4 += ",BusinessOwner1"
s4 += ",BusinessOwner2"
s4 += ",BusinessOwner3"
s4 += ",PropertyAddress1"
s4 += ",PropertyAddress2"
s4 += ",PropertyAddressCity"
s4 += ",PropertyAddressState"
s4 += ",PropertyAddressZip"
#        s1 = "{}, {}, {}, {}, {}, {}".format(os.path.basename(filename), member.filename, documentNumber, bookType, fileDate, fileTime)
#        s2 = "{}, {}, {}, {}, {}, {}".format(instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3)
#        s3 = "{}, {}, {}, {}, {}".format(propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip)
print s4
fileOut.writelines(s4 + "\n")

# askopenfilename() might return multiple files that were selected and should be iterated through.
for filename in filenames:
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
        s1 = '"{}", "{}", "{}", "{}", "{}", "{}"'.format(os.path.basename(filename), member.filename, documentNumber, bookType, fileDate, fileTime)
        #print s1
        #print filename, member.filename, documentNumber, bookType, fileDate, fileTime

        #04 Instrument Type:  UNINCORPORATED Comment:
        #   0123456789.123456789.123456789.123456789.123456789.123456789.
        #04 Instrument Type:  ABANDONMENT Comment:
        #05 # of Pages:  2
        #06 Business Owner
        #07
        #08 SW TRAILER RENTALS
        #09  RIVERA, DINAH ANN
        #10 RIVERA, RUDY RAUL
        try:
            cp = ad[4].index("Comment:")
            instrumentType = ad[4][18:cp - 1].strip()
            commentAD = ad[4][cp + 9:].strip()
        except:
            instrumentType = ""
            commentAD = ""
        numberOfPages = ad[5][11:].strip()
        # TODO; Might miss some business owners; can be multiple lines and ends before 1) blank line then 2) "Property Address"
        businessOwner1 = ad[8].strip()
        if businessOwner1 == "VOID, VOID VOID":
            print "Avoided " + businessOwner1 + ", " + s1
        else:
            businessOwner2 = ad[9].strip()
            businessOwner3 = ad[10].strip()
            s2 = '"{}", "{}", "{}", "{}", "{}", "{}"'.format(instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3)
            #print s1
            #print instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3

            #11
            #12 Property Address
            # "Property Address" (PA) can be on different lines skewing all following lines of data.
            # PA can start on line 11 and will go for as long as there are business owners. I'll capture 3 business owners, but there might be more.
            pa = 14
            for paln in range(11, 16):
                if ad[paln].strip() == "Property Address":
                    pa = paln
                    break
            #13
            #14 Address 1: .
            #   0123456789.123456789.123456789.123456789.123456789.123456789.
            #15 Address 2: 7407 CANOPUS BOW
            #16 City: SAN ANTONIO
            #17 State: TX
            #18 Zip: 78252-
            propertyAddress1 = ad[pa + 2][11:].strip()
            propertyAddress2 = ad[pa + 3][11:].strip()
            propertyAddressCity = ad[pa + 4][6:].strip()
            propertyAddressState = ad[pa + 5][7:].strip()
            propertyAddressZip = ad[pa + 6][5:].strip()
            s3 = '"{}", "{}", "{}", "{}", "{}"'.format(propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip)
            #print s1
            #print propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip
            # /home/dalem/Downloads/BEXAR_TXT_08142014.ZIP
            s4 = "{}, {}, {}".format(s1, s2, s3)
            print s4
            fileOut.writelines(s4 + "\n")
fileOut.close()
# TODO; work up mail/merge procedures for LibreOffice current version.
