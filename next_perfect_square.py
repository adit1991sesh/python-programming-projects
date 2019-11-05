#You might know some pretty large perfect squares. But what about the NEXT one?
#Complete the findNextSquare method that finds the next integral perfect square 
#after the one passed as a parameter. Recall that an integral perfect square is 
#an integer n such that sqrt(n) is also an integer. #If the parameter is itself 
#not a perfect square, than -1 should be returned. You may assume the parameter is positive.
#first trial
import math
import unittest

def find_next_square(sq):
# Return the next square if sq is a square, -1 otherwise
	sqrt = math.sqrt(sq)
	if sqrt.is_integer():
		sqrt = int(sqrt)
		if isinstance(sqrt,int):
			sqrt = sqrt + 1
			square = int(math.pow (sqrt, 2))
			return square
	else:
		return -1

print(find_next_square(4))

class Test(unittest.TestCase):
	def test_next_perfect_squares(self):
		self.assertEqual(find_next_square(121), 144, "121 is a perfect square and the next one is 144")
		self.assertEqual(find_next_square(625), 676, "625 is a perfect square and the next one is 676")
		self.assertEqual(find_next_square(319225), 320356, "319225 is a perfect square and the next one is 320356")
		self.assertEqual(find_next_square(15241383936), 15241630849, "15241383936 is a perfect square and the next one is 15241630849")

	def test_next_is_not_perfect_squares_return_negative_one(self):		
		self.assertEqual(find_next_square(155), -1, "155 is not a pefect square")
		self.assertEqual(find_next_square(342786627), -1, "342786627 is not a perfect square")

if __name__ == '__main__':
    unittest.main()
