import csv
import sqlite3

def options():
        print "Welcome to the Starlings Database. \nChose Numbers 1-6 to query the database. \nChose 7 to save changes. \nEnter -1 to quit."
        print"1) Choose to see all the tables in the database."
        print"2) Choose to see all the data from a table."
        print"3) Choose to see one or multiple columns from a table."
        print"4) Add Data"
        print"5) Update Data"
        print"6) Join Tables"
        print"7) Save changes to Database"
        num=int(raw_input("Type Number"))
        return num

def main():
    c = sqlite3.connect("/Users/afrazier/Desktop/Internship_Folder/Starlings.db")
    menu(c)

def allTable(c):
        results = c.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
        for row in results:
                print row
    
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

def joinTables(c):
        conn=c.cursor()
        table=raw_input("Please choose the first table you are joining.")
        column=raw_input("Please choose the column from that table.")
        table2=raw_input("Please choose the second table you are joining.")
        column2=raw_input("Please choose the column from that table.")
        results=c.execute("SELECT "+table+"."+column+", "+table2+"."+column2+" FROM Bird_Info JOIN "+table+" JOIN "+table2+" ON Bird_Info."+table+"_ID = "+table+"."+table+"_ID AND Bird_Info."+table+"_ID = "+table+"."+table+"_ID")
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


## Addin Data founctions
def printTable(c,table):
    results = c.execute("SELECT * FROM "+table)
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
        print rowASCII

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
    insertData(columnList,table,c,row)

def insertData(columnList,table,c,row=[]):
    numCols = len(columnList)
    inserts = ('?,'*(numCols+1))[:-1] # Saying what needs to be added to the table
    if row == []:
        c.execute('insert into '+table+' values ('+inserts+')',columnList)
    else:
        c.execute('insert into '+table+' values ('+inserts+')',columnList+[row[numCols]+1])
    printTable(c,table)

def getNewInfo(c):
    print "NOTE: if you do not have the data required, hit enter without typing anything.\n"
    printTable(c,"Identifiers")
    ident = raw_input("Identification: ")
    country = raw_input("Country: ")
    identifiers_ID = getTable([ident,country], "Identifiers", c)
    printTable(c,"Collection")
    collDate = raw_input("Collection Date: ")
    arrivDate = raw_input("Arrival Date: ")
    collector = raw_input("Collector: ")
    collection_ID = getTable([collDate,arrivDate,collector],"Collection",c)
    printTable(c,"Location")
    state = raw_input("State: ")
    county = raw_input("County: ")
    preciseLoc = raw_input("Precise Locality: ")
    lat = raw_input("Latitude: ")
    lon = raw_input("Longitude: ")
    location_ID = getTable([state,county,preciseLoc,lat,lon,collection_ID,identifiers_ID],"Location",c)
    printTable(c,"Death")
    prep = raw_input("Incoming Preparation: ")
    trap = raw_input("Trap Used: ")
    depredationMethod = raw_input("Depredation Method: ")
    death_ID = getTable([prep,trap,depredationMethod],"Death", c)
    printTable(c,"Preparation")
    specPrep = raw_input("Specimen Preparation Method: ")
    preparator = raw_input("Preparator: ")
    prep_ID = getTable([specPrep,preparator,death_ID],"Preparation",c)
    printTable(c,"Basic_Traits")
    fat = raw_input("Fat: ")
    age = raw_input("Age: ")
    sex = raw_input("Sex: ")
    basic_traits_ID = getTable([fat,age,sex],"Basic_Traits",c)
    printTable(c,"Complex_Traits")
    weight = raw_input("Weight: ")
    testesR = raw_input("Right Teste: ")
    testesL = raw_input("Left Teste: ")
    ovaries = raw_input("Ovaries: ")
    complex_traits_ID = getTable([weight,testesR,testesL,ovaries,basic_traits_ID],"Complex_Traits",c)
    pre_skin_ID = fillLengthInfo(c,"Pre_Skin")
    skin_ID = fillLengthInfo(c,"Skin")
    printTable(c,"Bird_Info")
    numRows = str(c.execute("SELECT COUNT(*) FROM Bird_Info"))
    insertData(["JMZ "+numRows,complex_traits_ID,location_ID,prep_ID,pre_skin_ID,skin_ID],"Bird_Info",c)

def fillLengthInfo(c,table):
    printTable(c,table)
    beak_length = raw_input(table + " Beak Length (in mm): ")
    beak_depth = raw_input(table + " Beak Depth (in mm): ")
    head_length = raw_input(table + " Head Length (in mm): ")
    wing_length = raw_input(table + " Wing Length (in mm): ")
    tail_length = raw_input(table + " Tail Length (in mm): ")
    tarsus_length = raw_input(table + " Tarsus Length (in mm): ")
    notes = raw_input("Any " + table + " notes on this bird: ")
    data_ID = getTable([beak_length,beak_depth,head_length,wing_length,tail_length,tarsus_length,notes],table,c)
    return data_ID


def menu(c):
    num=options()
    while num != -1:
        if num == 1:
                allTable(c)
        elif num == 2:
                tables(c)
        elif num == 4:
                getNewInfo(c)
        elif num == 5:
                updateData(c)
        elif num == 3:
                compareColumns(c)
        elif num == 6:
                joinTables(c)
        elif num == 7:
                save(c)
        else:
            print "Please chose another number."
        num=options()
    print "Thanks for using the Starlings Database."

main()



