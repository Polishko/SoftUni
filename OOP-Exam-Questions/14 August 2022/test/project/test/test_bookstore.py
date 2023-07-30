from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_correct_initialization(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_zero_or_below_book_limit_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_len_counts_books_correctly(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 4,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }
        result = len(self.bookstore)
        self.assertEqual(29, result)
        self.bookstore.availability_in_store_by_book_titles = {}
        result = len(self.bookstore)
        self.assertEqual(0, result)

    def test_receive_book_raises_error_if_capacity_full(self):
        self.bookstore.books_limit = 29
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 4,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Dukken I Taket", 5)
        self.assertEqual("Books limit is reached. Cannot receive more books!",
                         str(ex.exception))

        self.assertEqual({
            "The Girl With The Dragon Tattoo": 4,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_receives_books_correctly(self):
        self.bookstore.books_limit = 40
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }
        result = self.bookstore.receive_book("Dukken I Taket", 5)
        self.assertEqual({
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15,
            "Dukken I Taket": 5
        }, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("5 copies of Dukken I Taket"
                         " are available in the bookstore.", result)
        self.assertEqual(35, len(self.bookstore))

        result = self.bookstore.receive_book("The Girl With The Dragon Tattoo", 5)
        self.assertEqual({
            "The Girl With The Dragon Tattoo": 10,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15,
            "Dukken I Taket": 5
        }, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("10 copies of The Girl With The Dragon Tattoo"
                         " are available in the bookstore.", result)
        self.assertEqual(40, len(self.bookstore))

    def test_sell_book_raises_exception_for_unavailable_book(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("The Unbearable Lightness of Being", 3)
        self.assertEqual("Book The Unbearable Lightness of Being doesn't exist!",
                         str(ex.exception))
        self.assertEqual({
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_raises_exception_for_insufficient_book_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("The Master and Margarita", 15)
        self.assertEqual("The Master and Margarita has not enough copies to sell. "
                         "Left: 10",
                         str(ex.exception))
        self.assertEqual({
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_successful(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }
        result = self.bookstore.sell_book("The Master and Margarita", 4)
        self.assertEqual({
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 6,
            "Pippi Longstocking": 15
        }, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(4, self.bookstore.total_sold_books)
        self.assertEqual("Sold 4 copies of The Master and Margarita", result)

        result = self.bookstore.sell_book("The Girl With The Dragon Tattoo", 5)
        self.assertEqual({
            "The Girl With The Dragon Tattoo": 0,
            "The Master and Margarita": 6,
            "Pippi Longstocking": 15
        }, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(9, self.bookstore.total_sold_books)
        self.assertEqual("Sold 5 copies of The Girl With The Dragon Tattoo", result)

    def test_str_returns_correct_info(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "The Girl With The Dragon Tattoo": 5,
            "The Master and Margarita": 10,
            "Pippi Longstocking": 15
        }
        self.bookstore.sell_book("The Master and Margarita", 5)
        self.bookstore.sell_book("Pippi Longstocking", 3)
        self.bookstore.sell_book("Pippi Longstocking", 7)

        result = "Total sold books: 15\n" \
                 "Current availability: 15\n" \
                 " - The Girl With The Dragon Tattoo: 5 copies\n" \
                 " - The Master and Margarita: 5 copies\n" \
                 " - Pippi Longstocking: 5 copies"
        self.assertEqual(result, str(self.bookstore))


if __name__ == "__main__":
    main()
