"""
class MyObj(object):
	def __init__(self, num_loops):
		self.count = num_loops

	def go(self):
		for i in range(self.count):
			print i
		return
if __name__=='__main__':
	obj = MyObj(5)
	obj.go()


import pdb
class MyObj(object):
	def __init__(self, num_loops):
		self.count = num_loops

	def go(self):
		pdb.set_trace()
		for i in range(self.count):
			print i
		return
if __name__=='__main__':
	obj = MyObj(5)
	obj.go()#press "n" (next)and "c"(contunue) in cmd then "p i"(print i)then "q"(quit from pdb )

import pdb
class MyObj(object):
	def __init__(self, num_loops):
		self.count = num_loops
	def call_me(self):
		print("1")
		print("2")
		print("3")
	def go(self):
		pdb.set_trace()
		self.call_me()
		for i in range(self.count):
			print i
		return
if __name__=='__main__':
	obj = MyObj(5)
	obj.go()#"s"(step),"a"(detalis,argument),"j 36"(jump into 36 for this we "s""n")
"""

def KelvinToFahrenheit(Temperature):
	assert (Temperature >=0),"Colder than absolute zero!"
	return((Temperature-273)*1.8)+32
print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)




#python package
#piecham
