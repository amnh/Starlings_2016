import csv
import sqlite3

def options():
        print "Welcome to the Starlings Database. \nChose Numbers 1, 2, 3,4, or 6 to query the database. \nChose 5 to save changes. \nEnter -1 to quit."
        print"1) Choose to see all the data from a table."
        print"2) Choose to see a column from a table."
        print"3) Add Data"
        print"4) Update Data"
        print"5) Save changes to Database"
        print"6) Compare columns in a table" 
        num=int(raw_input("Type Number"))
        return num

def main():
    c = sqlite3.connect("/Users/afrazier/Desktop/Internship_Folder/Starlings.db")
    menu(c)
def tables(c):
    Table=raw_input("What table would you like?");
    results = c.execute("SELECT * From " + Table)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
            print(rowASCII)

def updateData(c):
    conn=c.cursor()
    table=raw_input("Please choose a table to alter.")
    number=raw_input("Which bird are you updating?")
    column=raw_input("What column are you changing?")
    newdata=raw_input("What are you changing?")
    conn.execute("UPDATE "+table+" SET "+column+" = '"+newdata+"' WHERE "+table+"_id in (SELECT "+table+"_id FROM Bird_Info WHERE Bird_Info.Number = '"+number+"')")
    results=c.execute("SELECT "+column+" FROM "+table+" WHERE "+table+"_id in (SELECT "+table+"_id FROM Bird_Info WHERE Bird_Info.Number = '"+number+"')")
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
    print(rowASCII)

def column(c):
    Tables=raw_input("What table would you like?")
    Column=raw_input("What column would you like?");
    results = c.execute("SELECT " + Column + " FROM " + Tables)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
        print(rowASCII)

def save(c):
       c.commit()

def compareColumns(c):
        Table = raw_input("What table would you like")
        Columns = raw_input("Type what columns you want to see. Please separate  them by commas.")
        results = c.execute("SELECT " + Columns + " FROM " + Table)
        for row in results:
                rowASCII=[]
                for item in row:
                        if type(item) == unicode:
                                rowASCII.append(item.encode('ascii'))
                else:
                        rowASCII.append(item)
                print (rowASCII)
                        
       
## Addin Data founctions
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

def menu(c):
    num=options()
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
            save(c)
        elif num == 6:
                compareColumns(c)
        else:
            print "Please chose another number."
        num=options()
    print "Thanks for using the Starlings Database."

main()



