
##for i in range(5):
##    name = raw_input("What's your name? ")
##    print "Hello", name
##
##    if name[0].upper() == "A":
##        print "Ayyyy!"
##    elif name[0].upper() == "E":
##        print "What is up my dude!"
##    elif name[0].upper() == "T":
##        print "Hola amiga!"
##    elif name[0].upper() == "L":
##        print "Waddup fam!"
##    else:
##            print "bye lmao"

import csv # Importing library

def getTable(columnList, table, c): # Defining a function, giving arguments that you need to use in the function
    results = c.execute("SELECT * FROM " + table) # RUnnning the query with user input
    numCols = len(columnList) # Finding the length of the column
    for row in results:
        ready = True
        print row
        for i in range(numCols):
            if row[i] != columnList[i]:
                ready = False # If the items in the rows don't match the user input, create a new row
        if ready == True:
            return row[numCols]
    inserts = ('?,'*(numCols+1))[:-1] # Saying what needs to be added to the table
    c.execute('insert into '+table+' values ('+inserts+')',columnList+[row[numCols]+1])
    printTable(table, c)

def printTable(table, c): # Defining a function
    results = c.execute("SELECT * FROM " + table)
    for row in results:
        print row


def getNewInfo(c):
    country = raw_input("Country: ")
    ident = raw_input("Identification: ")
    identifiers_ID = getTable([country, ident], "identifiers", c)
    collDate = raw_input("Collection Date: ")
    arrivDate = raw_input("Arrival Date: ")
    collector = raw_input("Collector: ")
    collection_ID = getTable([collDate,arrivDate,collector],"Collection",c)
    county = raw_input("County: ")
    state = raw_input("State: ")
    preciseLoc = raw_input("Precise Locality: ")
    lat = raw_input("Latitude: ")
    lon = raw_input("Longitude: ")
    location_ID = getTable([county,state,preciseLoc,lat,lon,identifiers_ID,collection_ID],"Location",c)
    # New information that needs to be added to the data using user input for the location table and all connected to it


def testcsv():
    s = open("/Users/eleon/Desktop/Starlings/StarlingData.csv", "rU") # Opening the CSV
    starlingfile = csv.reader(s) # Reading
#   for row in starlingfile:
#       print row
    data = list(starlingfile)
    for row in data:
        print row[0]
    #Printing the info in the file

def options():
    print "Please enter what you'd like to do by typing the corresponding numbers."
    print "Your options are to show all the data, select a certain part of the data, or add new data."
    print "To quit, type -1"
    num = int(raw_input("What would you like to do?"))
    return num
    # Presents the options to the user

import sqlite3 # Importing library

def connection():
    conn = sqlite3.connect("/Users/eleon/Desktop/Starlings/Starlings.db")
    results = conn.execute("SELECT OVARIES FROM Complex_Traits;")
    for row in results:
            print row
    # SQLite connection
            
    conn.close() # Closing connection

def menu(c):
    num = options()
    while num != -1:
        if num == 1:
            testcsv()
        elif num == 2:
            #connection()
            table = raw_input("table? ")
            printTable(table,c)
        elif num == 3:
            getNewInfo(c)
        else:
            print "Just go home..."
        num = options()
        print "Goodbye!"
    # Menu, what to do with the user input

def main():
    c = sqlite3.connect("/Users/eleon/Desktop/Starlings/Starlings.db") # Connection
    menu(c) # Goes to menu

main()
