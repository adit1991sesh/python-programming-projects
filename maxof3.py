#Implement a function that takes as input three variables, and returns the largest of the three. 
#Do this without using the Python max() function! The goal of this exercise is to think about some 
#internals that Python normally takes care of for us. All you need is some variables and if statements!

import unittest

def findMaxOfThreeVariables(variable1, variable2, variable3):
	if variable1 > variable2 and variable1 > variable3:
		return variable1
	elif variable2 > variable1 and variable2 > variable3:
		return variable2
	else:
		return variable3

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(findMaxOfThreeVariables(5, 3, 2), 5)
        self.assertEqual(findMaxOfThreeVariables(1, 1, 1), 1)
        self.assertEqual(findMaxOfThreeVariables(0, 0, 0), 0)
        self.assertEqual(findMaxOfThreeVariables(-1, 45, 10), 45)
        self.assertEqual(findMaxOfThreeVariables(10, 20, 30), 30)
        self.assertEqual(findMaxOfThreeVariables(-2, 45, -10), 45)
        self.assertEqual(findMaxOfThreeVariables(0, 0, 10), 10)

if __name__ == '__main__':
    unittest.main()






