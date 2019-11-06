#you are asked to square every digit of a number.For example, if we run 9119 
#through the function, 811181 will come out, because 92 is 81 and 12 is 1.

import math
import unittest

def square_digits(num):
	nums = []
	number = str(num)
	for digit in number:
		digit=int(math.pow(int(digit),2))		
		nums.append(digit)
		new_number = (str(nums)[1:-1]).replace(',', '')
		new_number = int(new_number.replace(' ', ''))
	return new_number

class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(square_digits(9), 81)
		self.assertEqual(square_digits(91), 811)
		self.assertEqual(square_digits(911), 8111)
		self.assertEqual(square_digits(9119), 811181)

if __name__ == '__main__':
    unittest.main()

