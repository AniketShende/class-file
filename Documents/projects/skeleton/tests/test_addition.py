import unittest
from NAME import calculation
class TestStringMethod(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(caluclation.addition(1,2),1+2)
	
if __name__ == '__main__':
	unittest.main()
