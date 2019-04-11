'''
import sqlite3 # create update read and delete
print(sqlite3.version)
print(sqlite3.sqlite_version)
import sqlite3
db=sqlite3.connect('test.db')
db.close()
'''

import sqlite3
db=sqlite3.connect('test.db')
cursor=db.cursor()
#cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, price TEXT, year TEXT)''')
title1='Learning Python'
author1='Mark Lutz'
price1='$36.19'
year1='Jul 6,2013'
title2='Two Scoops of Django: Best practices for Django 1.6'
author2='Daniel Greenfeld'
price2='$34.68'
year2='Feb 1,2014'
title3='Python Coockbook'
author3='David Beazley'
price3='$30.29'
year3='May 29, 2013'
cursor.execute('''INSERT INTO books(title,author, price,year)VALUES(?,?,?,?)''',(title1,author1,price1,year1))
cursor.execute('''INSERT INTO books(title,author, price,year)VALUES(?,?,?,?)''',(title2,author2,price2,year2))
cursor.execute('''INSERT INTO books(title,author, price,year)VALUES(:title, :author, :price, :year)''',{'title':title3, 'author':author3, 'price': price3, 'year':year3})
db.commit()
db.close()

'''
import sqlite3
db=sqlite3.connect('test.db')
cursor=db.cursor()
delete_book_id=1
cursor.execute('''DELETE FROM books WHERE id =?''',
(delete_book_id,)) 
db.commit()
cursor.execute('''SELECT title, author, price FROM books''')
all_books=cursor.fetchall()
for book in all_books:
	print(book)
db.close()
'''

'''
import sqlite3
db=sqlite3.connect('test.db')
cursor=db.cursor()
#cursor.execute('''UPDATE books SET price=? WHERE id =?''',(3,2)) 
db.commit()
cursor.execute('''SELECT title, author, price FROM books''')
all_books=cursor.fetchall()
for book in all_books:
	print(book)
db.close()
import sqlite3
db=sqlite3.connect('test.db')
cursor=db.cursor()
#cursor.execute('''SELECT title, author, price FROM books WHERE id=?''',(2,))
book1 = cursor.fetchone()
print(book1)
all_cols=cursor.fetchall()
for row in all_cols:
	print(row)
db.commit()
db.close()
'''
'''
import sqlite3
db=sqlite3.connect('test.db')
cursor=db.cursor()
cursor.execute('''DROP TABLE books''')
db.commit()
db.close()
'''

import MySQLdb
db=MySQLdb.connect("localhost","root","root","testDB")
cursor=db.cursor()
sql="ALTER TABLE STUDENT ADD TOWN VARCHAR(15)"
try:
	#Execute the SQL command
	cursor.execute(sql)
	#Commit your changes in the database
except:
	#Rollback in case there is any error
	db.rollback()
else:
	print("number of rows affected {0}".format(cursor.rowcount))
	db.commit()
#disconnect form server
finally:
	db.close()
