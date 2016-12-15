def allTable(c):
        results = c.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
        for row in results:
                print row 
