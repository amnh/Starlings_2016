import sqlite3
def updateData():
    conn=sqlite3.connect('Starlings.db')
    c=conn.cursor()
    table=raw_input("Please choose a table to alter.")
    number=raw_input("Which bird are you updating?")
    column=raw_input("What column are you changing?")
    newdata=raw_input("What are you changing?")
    c.execute("UPDATE "+table+" SET "+column+" = '"+newdata+"' WHERE "+table+"_id in (SELECT "+table+"_id FROM Bird_Info WHERE Bird_Info.Number = '"+number+"')")
    results=c.execute("SELECT "+column+" FROM "+table+" WHERE "+table+"_id in (SELECT "+table+"_id FROM Bird_Info WHERE Bird_Info.Number = '"+number+"')")
    for row in results:
        rowASCII=[]
        for item in row:
            if type(item) == unicode:
                rowASCII.append(item.encode('ascii'))
            else:
                rowASCII.append(item)
    print(rowASCII)
    conn.commit()
    conn.close()
updateData()

def joinTables():
    conn=sqlite3.connect('Starlings.db')
    c=conn.cursor()
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
    conn.close()
joinTables()

def showTables(c):
        c.execute("SELECT * FROM sqlite_master WHERE type= 'table'")

