import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_book_1(self):
        book1 = data.Book("Drew", "Hello")
        book2 = data.Book("Drew", "Zoot")
        book3 = data.Book("Drew", "Banana")
        input = [book1, book2, book3]
        expected = [book3, book1, book2]
        self.assertEqual(expected, lab6.selection_sort_books(input))

    def test_selection_sort_book_2(self):
        input = []
        expected = []
        self.assertEqual(expected, lab6.selection_sort_books(input))
    # Part 2
    def test_swap_case_1(self):
        input = "Hello"
        expected = "hELLO"
        self.assertEqual(expected, lab6.swap_case(input))

    def test_swap_case_2(self):
        input = "Hриве"
        expected = "Hриве"
        self.assertEqual(expected, lab6.swap_case(input))
    # Part 3
    def test_str_translate_1(self):
        input = "hello"
        old = 'l'
        new = 'x'
        self.assertEqual("hexxo", lab6.str_translate(input, old, new))

    def test_str_translate_2(self):
        input = ""
        old = 'c'
        new = 'x'
        self.assertEqual("", lab6.str_translate(input, old, new))

    # Part 4
    def test_histogram_1(self):
        input = "Hello my name is Drew"
        self.assertEqual({'Hello': 1, 'my': 1,'name':1, 'is': 1, 'Drew':1 }, lab6.histogram(input))

    def test_histogram_2(self):
        input = "Hello my name is Drew Drew Drew Drew Drew Drew Drew"
        self.assertEqual({'Hello': 1, 'my': 1,'name':1, 'is': 1, 'Drew':7 }, lab6.histogram(input))






if __name__ == '__main__':
    unittest.main()
