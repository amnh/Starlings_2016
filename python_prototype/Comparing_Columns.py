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
