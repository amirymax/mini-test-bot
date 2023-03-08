import sqlite3

sqlite_con = sqlite3.connect('data.db')
cursor = sqlite_con.cursor()
print('database sozdan')

cursor.execute("CREATE TABLE biology(savol TEXT,v1 TEXT,v2 TEXT,v3 TEXT);")
# cursor.execute('SELECT * FROM math')
s = cursor.fetchall()
cursor.close()
sqlite_con.close()

# sqlite_con.commit()
