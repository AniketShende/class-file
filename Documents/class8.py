"""
class company():				#class name
	class_variable = "ABC"			#class variable
	def __init__(self, name, location):	#like main
		self.name_value = name		#initialize value
		self.location_value = location
	def name (self):
		print(self.name_value)
		print(self.class_variable)
	def location (self):
		print(self.location_value)
	def profile(self):
		print("name:{0}".format(self.name_value))
		print("location:{0}".format(self.location_value))
		print("name: "+self.name_value)
		#self.class_variable="xyz"
TaTa=company("TaTa","Pune")			#object creation
TaTa.name()					#function call
TaTa.location()
TaTa.profile()
print(TaTa.name_value)#object variable
print(TaTa.location_value)

class company():
	class_variable="ABC"
	def __init__(self,name,location):
		self.name_value = name
		self.location_value = location
	def name(self):
		print(self.name_value)
		print(self.class_variable)
	def location:
		print(self.location_value)


"""
class Company(object):
	def __init__(self, *args):
		if len(args) == 3:
			self.cname = args[0]
			self.city = args[1]
			self.name = args[2]
			print(self.cname, self.city, self.name)
		elif len(args) == 2:
			self.city=args[0]
			self.country=args[1]
			#self.city=""
			print(self.city, self.country)

TaTa=Company("TaTa","Pune","India")
Mahindra = Company("Mahindra","Pune")
#obj = Company()



