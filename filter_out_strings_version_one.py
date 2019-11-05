#filters out strings an returns the array filled with numbers

#First attempt
import unittest
def filter_list(l):
    new_l = []
    for value in l:
        if isinstance(value, int):
            new_l.append(int(value))
    return new_l

print(filter_list([10,2,50,77,'abd','ccd',89,100]))
print(filter_list([1,2,'a','b']))

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(filter_list([1,2,'a','b']),[1,2])
        self.assertEqual(filter_list([1,'a','b',0,15]),[1,0,15])
        self.assertEqual(filter_list([1,2,'aasf','1','223',123]),[1,2,123])

if __name__ == '__main__':
    unittest.main()


