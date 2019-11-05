#filters out strings an returns the array filled with numbers

#Second attempt
import unittest

def filter_list(listofnumbers):
    filteredList = [value for value in listofnumbers if isinstance(value, int)]
    return filteredList

print(filter_list([10,2,50,77,'abd','ccd',89,100]))
print(filter_list([1,2,'a','b']))

class Test(unittest.TestCase):

    def test_only_single_alphabets(self):
        self.assertEqual(filter_list([1,2,'a','b']),[1,2])
        self.assertEqual(filter_list([1,'a','b',0,15]),[1,0,15])
        self.assertEqual(filter_list(['g',1,5,7,'d',334]),[1,5,7,334])
    def test_only_more_than_one_letter(self):
        self.assertEqual(filter_list([1,2,'aasf','gg','time',123]),[1,2,123])
        self.assertEqual(filter_list([1,77, 45, 'aasf','happy',123, 'romance']),[1,77,45,123])
    def test_number_as_strings(self):
        self.assertEqual(filter_list(['1',23,44,'89']), [23,44])
        self.assertEqual(filter_list(['1','23', '22', 22, 44, 1,'89']), [22,44,1])
        
if __name__ == '__main__':
    unittest.main()
