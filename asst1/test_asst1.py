import unittest 
from asst1 import swapchars, bluesclues, bluesbooze, sortcat

class TestString(unittest.TestCase):
	def test_swapchars(self):
		self.assertEqual(swapchars('I\'m just a chi-town coder with a nice flow.'), 'U\'m jist a chu-town coder wuth a nuce flow.')
		self.assertEqual(swapchars("hellooooo"), 'holleeeee')
		self.assertEqual(swapchars("HHHHHHHelloh"), 'OOOOOOOellho')

	def test_bluesclues(self):
		self.assertEqual(bluesclues('MA'), 'Massachusetts')
		self.assertEqual(bluesclues('CA'), 'California')
		self.assertEqual(bluesclues('AL'), 'Alabama')
	
	def test_bluesbooze(self): 
		self.assertEqual(bluesbooze('Massachusetts'), 'MA')
		self.assertEqual(bluesbooze('New York'), 'NY')
		self.assertEqual(bluesbooze('Hawaii'), 'HA')
	
	def test_sortcat(self): 
		self.assertEqual(sortcat(1, 'abc', 'bc'), 'abc')
		self.assertEqual(sortcat(2, 'abc','abcd','bb'), 'abcdabc')
		self.assertEqual(sortcat(-1, 'abc', 'abcd'), 'abcdabc')

if __name__ == '__main__':
	unittest.main()