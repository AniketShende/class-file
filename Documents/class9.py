"""  #Exception
try:
	file_obj = open("test data.txt")
	print(file_obj.read())
	print(1/0)
	print(a)

except IOError:	
	file_obj = open("test data.txt","w")
	file_obj.write("this is test data")
except ZeroDivisionError:
	print("ZeroDivisionError")
	print("plz dont divide with zero")
except Exception as err:
	print(err)

#=================================================

try:
	file_obj = open("test data.txt")
	print(file_obj.read())
	#print(1/0)
	#print(a)

except IOError:	
	file_obj = open("test data.txt","w")
	file_obj.write("this is test data")
except ZeroDivisionError:
	print("ZeroDivisionError")
	print("plz dont divide with zero")
except Exception as err:
	print(err)

else:#if error is not present
	print("this shows no error")
finally:#executed all the time
	print("this is a block which execute all the time")
	#file.close()


#============================================================
#not do for try and except(dont use try in nested form)

try:
	fh = open("testfile","w")
	try:
		fh.write("This is my test file for exception handeling")
		print(fh.read())
	finally:
		print "Going to close the file"
		fh.close()
except IOError:
	print "Error: can\'t find file or read data"

#==============================================================





class MinimumValueError(Exception):
	#Constructor or Initializer
	def __init__(self, value):
		self.value = value
	#str is to print()the value
	def __str__(self):
		return(repr(self.value))# repr:-convert the numeric value into string

try:
	value = int(input("pls input value greater than 0"))
	if value < 0:
		raise(MinimumValueError(value))#if u want to generate exception raise is used
except MinimumValueError as err:
	print("this is an invalid value: {0}".format(err.value))



#===============hw==========
#can we write try statement with out except?
#install:-
#picham comunity version
#nose module 
#1.python get.pip.py
#2.pip(cmd)
#3.pip install nose
"""

