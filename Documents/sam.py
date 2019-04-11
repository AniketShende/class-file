"""
class main():
	def __init__(self,name,location):
		self.a=name
		self.b=location
		print(self.a)
		#print(a)
		print (self.b)
Aniket=main("Aniket","Pune")
"""

class main():
	def __init__(self,location,imp_places):
		self.a=location
		self.b=imp_places
		print(self.a, self.b)
	def loc(self):
		print("you are in the loc block "+self.a)
Hyd=main("Hyderabad","Birla temple")
Hyd.loc()
Hyd.loc()
