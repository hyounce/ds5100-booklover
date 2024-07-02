from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        book_lover1 = BookLover('Hilde', 'ksg8xy@virginia.edu', 'romance')
        book_lover1.add_book('Dune', 5)
        books = book_lover1.book_list['book_name'].tolist()
        actual = 'Dune' in books
        message = "Book was not added successfully"
        self.assertTrue(actual, message)
    
    def test_2_add_book(self):
        book_lover2 = BookLover('Hilde', 'ksg8xy@virginia.edu', 'romance')
        book_lover2.add_book('Dune', 5)
        book_lover2.add_book('Dune', 5)
        books = book_lover2.book_list['book_name'].tolist()
        actual = sum([True for book in books if book == 'Dune'])
        message = "Same book was added more than once."
        self.assertLess(actual, 2)    
    
    def test_3_has_read(self):
        book_lover3 = BookLover('Hilde', 'ksg8xy@virginia.edu', 'romance')
        book_lover3.add_book('Dune', 5)
        books = book_lover3.book_list['book_name'].tolist()
        actual = 'Dune' in books
        message = "Book not found in book list."
        self.assertTrue(actual, message)

    def test_4_has_read(self):
        book_lover4 = BookLover('Hilde', 'ksg8xy@virginia.edu', 'romance')
        books = book_lover4.book_list['book_name'].tolist()
        actual = 'Dune' in books
        message = "Unread book found in book list."
        self.assertFalse(actual, message)

    def test_5_num_book_read(self):
        book_lover5 = BookLover('Hilde', 'ksg8xy@virginia.edu', 'romance')
        book_lover5.add_book('Dune', 5)
        book_lover5.add_book('Emma', 5)
        book_lover5.add_book('The Great Gatsby', 5)
        expected = 3
        actual = book_lover5.num_books
        message = "Number of books in list does not match num_books."
        self.assertEqual(expected, actual, message)
    
    def test_6_fav_books(self):
        book_lover6 = BookLover('Hilde', 'ksg8xy@virginia.edu', 'romance')
        book_lover6.add_book('Dune', 5)
        book_lover6.add_book('Emma', 3)
        book_lover6.add_book('The Great Gatsby', 4)
        book_ratings = book_lover6.fav_books()['book_rating'].tolist()
        expected = 2
        actual = sum([True for rating in book_ratings if rating > 3])
        message = "Books in fav_books do not have ratings > 3"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(verbosity=3)

