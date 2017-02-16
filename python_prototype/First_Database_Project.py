import csv
import sqlite3

def column():
    conn = sqlite3.connect("/Users/afrazier/Desktop/Internship_Folder/Starlings.db")
    Tables=raw_input("What table would you like?")
    Column=raw_input("What column would you like?");
    results = conn.execute ("SELECT " + Column + " FROM " + Tables)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
        print(rowASCII)

def tables():
    conn = sqlite3.connect("/Users/afrazier/Desktop/Internship_Folder/Starlings.db")
    Table=raw_input("What table would you like?");
    results = c.execute ("SELECT * From " + Table)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
            print(rowASCII)

##def prep():
##    conn = sqlite3.connect("/Users/afrazier/Desktop/Internship_Folder/Starlings.db")
##    Columns=raw_input("What column would you like?");
##    results = conn.excute ("SELECT" + Column + "FROM Preparation")
##    for row in results:
##        print row
def options():
        print "Welcome to the Starlings Database. \nChose Numbers 1 or 2 to search the database. \nEnter -1 to quit."
        print"1) Choose to see all the data from a table."
        print"2) Choose to see a column from a table."
        num=int(raw_input("Type Number"))
        return num
def menu():
    num=options()
    while num != -1:
        if num == 1:
            tables()
        elif num == 2:
            column()
        else:
            print "Still Updating"
        num=options()
    print "Thanks for using the Starlings Database."

menu()




    
