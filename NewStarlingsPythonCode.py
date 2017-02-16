import csv
import sqlite3

def options():
    print "Welcome to the Starlings Database. \nChose number 1, 2, 3, 4, or 5 to select what you'd like to do. \nEnter -1 to quit."
    print "1) Choose to see all the data from a table."
    print "2) Choose to see a column from a table."
    print "3) Add data."
    print "4) Update data."
    print "5) Save."
    num = int(raw_input("What would you like to do? Please enter your number. "))
    return num

def main():
    c = sqlite3.connect("/Users/eleon/Desktop/Starlings/Starlings.db")
    menu(c)

def menu(c):
    num = options()
    while num != -1:
        if num == 1:
            tables(c)
        elif num == 2:
            column(c)
        elif num == 3:
            getNewInfo(c)
        elif num == 4:
            updateData(c)            
        elif num == 5:
            c.commit()
        else:
            print "Please pick an option."
        num = options()
    print "Thank you for using the Starlings Database! \nGoodbye!"

# OPTION NUMBER 1
def tables(c):
    Table=raw_input("What table would you like to see? ");
    results = c.execute ("SELECT * From " + Table)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
            print(rowASCII)

#OPTION NUMBER 2
def column(c):
    Tables=raw_input("What table is your column in? ")
    Column=raw_input("What column would you like to see? ");
    results = c.execute ("SELECT " + Column + " FROM " + Tables)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
        print(rowASCII)

#OPTION NUMBER 3
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

#OPTION NUMBER 4
def updateData(c):
    conn=c.cursor()
    table=raw_input("Please choose a table to alter. ")
    number=raw_input("Which bird are you updating? ")
    column=raw_input("What column are you changing? ")
    newdata=raw_input("What are you changing? ")
    conn.execute("UPDATE "+table+" SET "+column+" = '"+newdata+"' WHERE "+table+"_id in (SELECT "+table+"_id FROM Bird_Info WHERE Bird_Info.Number = '"+number+"')")
    results=conn.execute("SELECT "+column+" FROM "+table+" WHERE "+table+"_id in (SELECT "+table+"_id FROM Bird_Info WHERE Bird_Info.Number = '"+number+"')")
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
    print(rowASCII)

main()
