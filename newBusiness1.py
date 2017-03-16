# python3 newBusiness1.py
# See: infoNewBusiness.txt for more information.

__author__ = 'DaleEMoore@gMail.Com'

import os

#Select ZIP file from Downloads
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
    from tkFileDialog import askopenfilename
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too
    from tkinter.filedialog import askopenfilename
    #from tkinter import filedialog
#from Tkinter import Tk
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# keep the last folder used for the next run. (Maybe http://goo.gl/2lkJV0) or default to ~/Downloads.
# default to files named *.ZIP. (Lots of info here http://tkinter.unpythonic.net/wiki/tkFileDialog)
# Cool: http://nullege.com/codes/show/src@k@a@kamaelia-HEAD@Code@Python@Kamaelia@Kamaelia@Apps@Whiteboard@Decks.py/123/Tkinter.Tk.withdraw
# TODO; persist theDir from previous run? Read my question here
# http://programmers.stackexchange.com/questions/253527/where-to-save-something-between-invocations?noredirect=1#comment510007_253527
# appdirs (https://pypi.python.org/pypi/appdirs/1.4.0) might be best part of figuring out where to save the data.
theDir = "~/Downloads"
#if exists(askopenfilename):
filenames = askopenfilename(multiple=1,filetypes=[("Zip Archives",("*.zip", "*.ZIP"))],initialdir=theDir,title="Businesses ZIP with TXTs")
#else:
#    filenames = askopenfilename(multiple=1,filetypes=[("Zip Archives",("*.zip", "*.ZIP"))],initialdir=theDir,title="Businesses ZIP with TXTs")

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
print (fileOutName)
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
print (s4)
fileOut.writelines(s4 + "\n")

# askopenfilename() might return multiple files that were selected and should be iterated through.
for filename in filenames:
    #Pull out TXT file(s)
    import zipfile
    file = zipfile.ZipFile(filename)
    #file = zipfile.ZipFile(filename, mode='r')
    zipMembers = file.infolist()

    #Process each TXT file extracting data and exporting into LibreOffice Database.
    for member in zipMembers:
        #print member, member.filename, member.orig_filename, member.date_time
        rd = file.read(member)
        #rd = file.read(member,"r")
        # if file contains "  Internet Explorer cannot display the webpage " skip it.
        # TODO; I do not know if the following is still relevent.
        # File "/home/dalem/PycharmProjects/newBusiness1/newBusiness1.py", line 128, in <module>
        #   if rd.find(" Internet Explorer cannot display the webpage ") != -1:
        #   TypeError: 'str' does not support the buffer interface
        #if rd.find(" Internet Explorer cannot display the webpage ") != -1:
        #    # TODO; you have to remember to look at the console messages to see these.
        #    # TODO; add counters showing the number of empty @ end of console run.
        #    print (str(member.filename) + " is empty.")
        #    continue
        #print rd
        ad = rd.splitlines()
        #00 General Information
        #01
        #02 Document Number:  20140486166 Book Type:  ASSUMED NAMES
        #03 Filed Date:  8/14/2014 Filing Time:  4:43 PM
        documentNumber = ad[2][18:29].strip().decode("utf-8")
        bookType = ad[2][42:].strip().decode("utf-8")
        fileDate = ad[3][12:22].strip().decode("utf-8")
        fileTime = ad[3][36:].strip().decode("utf-8")
        #Fr 20 May 2016 8:37 AM CST, getting b'<data>' on fields DocumentNumber, bookType, fileDate, fileTime, NumberOfPages, BusinessOwner1, BusinessOwner2, BusinessOwner3, and others...
        # It didn't used to get the "b'<data>'" surrounding <data>. What's changed? Python3 now outputs the type surrounding or it's changed it's defaults?
        # Maybe it used to be Python2 and I've not noticed the different output since converting to Python3.
        # DocumentNumber.decode('utf-8')?
        # Fix: after every .strip().decode("utf=8")
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
            instrumentType = ad[4][18:cp - 1].strip().decode("utf-8")
            commentAD = ad[4][cp + 9:].strip().decode("utf-8")
        except:
            instrumentType = ""
            commentAD = ""
        try:
            numberOfPages = ad[5][11:].strip().decode("utf-8")
        except:
            # probably because there aren't this many lines in the .TXT file.
            numberOfPages = 0 # TODO; some better error reporting is called for here.
        # TODO; Might miss some business owners; can be multiple lines and ends before 1) blank line then 2) "Property Address"
        try:
            businessOwner1 = ad[8].strip().decode("utf-8")
        except:
            # probably because there aren't this many lines in the .TXT file.
            businessOwner1 = "*** Too few lines in .TXT file!"
        if businessOwner1 == "VOID, VOID VOID":
            print ("Avoided " + businessOwner1 + ", " + s1)
        else:
            try:
                businessOwner2 = ad[9].strip().decode("utf-8")
            except:
                businessOwner2 = "*** Too few lines in .TXT file!"
            try:
                businessOwner3 = ad[10].strip().decode("utf-8")
            except:
                businessOwner3 = "*** Too few lines in .TXT file!"
            s2 = '"{}", "{}", "{}", "{}", "{}", "{}"'.format(instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3)
            #print s1
            #print instrumentType, commentAD, numberOfPages, businessOwner1, businessOwner2, businessOwner3

            #11
            #12 Property Address
            # "Property Address" (PA) can be on different lines skewing all following lines of data.
            # PA can start on line 11 and will go for as long as there are business owners. I'll capture 3 business owners, but there might be more.
            pa = 14
            imin = 11
            imax = 16
            if len(ad) < imax:
                imax=len(ad)


            """
                TODO; Handle the Property Address section differently!
                The Property Address section looks like:
                Property Address

                Address 1: .
                Address 2: 11400 CULEBRA #204
                City: SAN ANTONIO
                State: TX
                Zip: 78254-
                I should look for “Property Address”, skip the blank line then process.
            """

            for paln in range(imin, imax):
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
            propertyAddress1 = propertyAddress2 = propertyAddressCity = propertyAddressState = propertyAddressZip = ""
            # sometimes the property address is missing.
            try:
                propertyAddress1 = ad[pa + 2][11:].strip().decode("utf-8")
                propertyAddress2 = ad[pa + 3][11:].strip().decode("utf-8")
                propertyAddressCity = ad[pa + 4][6:].strip().decode("utf-8")
                propertyAddressState = ad[pa + 5][7:].strip().decode("utf-8")
                propertyAddressZip = ad[pa + 6][5:].strip().decode("utf-8")
            except:
                pass
            s3 = '"{}", "{}", "{}", "{}", "{}"'.format(propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip)
            #print s1
            #print propertyAddress1, propertyAddress2, propertyAddressCity, propertyAddressState, propertyAddressZip
            # /home/dalem/Downloads/BEXAR_TXT_08142014.ZIP
            s4 = "{}, {}, {}".format(s1, s2, s3)
            print (s4)

            # TODO; lookup phone numbers for this entity.
            """
            Search for BusinessOwner1 + PropertyAddress2 (Not if PO Box) + PropertyCity + PropertyState + PropertyZip + ", phone"
            Maybe 'Google Place API' is a good place to start, thought I don't think so.

            """

            fileOut.writelines(s4 + "\n")
fileOut.close()
# TODO; work up mail/merge procedures for LibreOffice current version.
