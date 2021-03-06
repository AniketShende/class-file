"""
s="hello world"
print(s.split())
print(s.split("l"))
print(s.split(2))
"""

import unittest
class TestStringMethod(unittest.TestCase):
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
	def test_split(self):
		s="hello world"
		self.assertEqual(s.split(),['hello','world'])
		with self.assertRaises(TypeError):
			s.split(2)
if __name__ == '__main__'
	unittest.main()
