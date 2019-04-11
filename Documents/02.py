'''
import MySQLdb
db=MySQLdb.connect("localhost","root","root","testDB")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS STUDENT")
sql="""CREATE TABLE STUDENT(FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20),AGE INT, SEX CHAR(1),PERCENTAGE FLOAT)"""
cursor.execute(sql)
db.commit()
db.close()
'''
'''
import MySQLdb
db=MySQLdb.connect("localhost","root","root","testDB")
cursor=db.cursor()
sql="""INSERT INTO STUDENT(FIRST_NAME,LAST_NAME,AGE,SEX,PERCENTAGE) VALUES('%s', '%s','%d', '%c','%f')""" % ('Mac','Mohan',20,'M',56)
try:
	#Execute the SQL command
	cursor.execute(sql)
	#Commit your changes in the database
except:
	#Rollback in case there is any error
	db.rollback()
else:
	db.commit()
#disconnect form server
finally:
	db.close()
'''
'''
import MySQLdb
db=MySQLdb.connect("localhost","root","root","testDB")
cursor=db.cursor()
sql="SELECT * FROM STUDENT WHERE PERCENTAGE= '%f' " % (56)
try:
	#Execute the SQL command
	cursor.execute(sql)
	#Commit your changes in the database
except:
	#Rollback in case there is any error
	db.rollback()
else:
	fetch_one_record=cursor.fetchone()
	print (fetch_one_record)
	fetch_all=cursor.fetchall()
	for row in fetch_all:
		print(row)
	db.commit()
#disconnect form server
finally:
	db.close()
'''
'''
import MySQLdb
db=MySQLdb.connect("localhost","root","root","testDB")
cursor=db.cursor()
sql="UPDATE STUDENT SET PERCENTAGE = 70 WHERE PERCENTAGE<'%f' " % (60)
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
'''
'''
import MySQLdb
db=MySQLdb.connect("localhost","root","root","testDB")
cursor=db.cursor()
sql="DELETE FROM STUDENT WHERE FIRST_NAME = Mac"
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
