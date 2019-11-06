import unittest

def sort_array(source_array):
	odd = iter(sorted(number for number in source_array if number%2 != 0))
	sorted_list = [next(odd) if number%2 else number for number in source_array]

	return sorted_list


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
        self.assertEqual(sort_array([]),[])

if __name__ == '__main__':
    unittest.main()


