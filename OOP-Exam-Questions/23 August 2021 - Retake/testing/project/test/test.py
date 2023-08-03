from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library1 = Library("library1")
        self.library1.books_by_authors = {
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"]
        }
        self.library1.readers = {
            "reader1": [],
            "reader2": [],
            "reader3": []
        }
        self.library2 = Library("emptylibrary")

    def test_correct_initialisation(self):
        self.assertEqual("library1", self.library1.name)
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"]
        }, self.library1.books_by_authors)
        self.assertEqual({
            "reader1": [],
            "reader2": [],
            "reader3": []
        }, self.library1.readers)
        self.assertEqual({}, self.library2.books_by_authors)
        self.assertEqual({}, self.library2.readers)

    def test_empty_string_name_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library1.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            Library("")
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_resetting_name_sets_name_correctly(self):
        self.library1.name = "newlibraryname"
        self.assertEqual("newlibraryname", self.library1.name)

    def test_add_book_adds_books_and_titles_correctly(self):
        # add new author and new book
        self.library1.add_book("author4", "book1")
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"],
            "author4": ["book1"]
        }, self.library1.books_by_authors)

        # add empty name new author
        self.library1.add_book("", "book1")
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"],
            "author4": ["book1"],
            "": ["book1"]
        }, self.library1.books_by_authors)

        # add empty title to existing empty author
        self.library1.add_book("", "")
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"],
            "author4": ["book1"],
            "": ["book1", ""]
        }, self.library1.books_by_authors)

        # try adding existing book to existing author
        self.library1.add_book("author1", "book1")
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"],
            "author4": ["book1"],
            "": ["book1", ""]
        }, self.library1.books_by_authors)

        # add new book to existing author
        self.library1.add_book("author1", "book5")
        self.assertEqual({
            "author1": ["book1", "book2", "book3", "book5"],
            "author2": ["book4", "book5"],
            "author3": ["book6"],
            "author4": ["book1"],
            "": ["book1", ""]
        }, self.library1.books_by_authors)

        # add book and author to empty library
        self.library2.add_book("author1", "book2")
        self.assertEqual({
            "author1": ["book2"],
        }, self.library2.books_by_authors)

        # add same book title to another author
        self.library2.add_book("author2", "book2")
        self.assertEqual({
            "author1": ["book2"],
            "author2": ["book2"]
        }, self.library2.books_by_authors)

    def test_add_reader_works_properly(self):
        # add to empty reader attr
        result = self.library2.add_reader("reader1")
        self.assertEqual({"reader1": []}, self.library2.readers)
        self.assertEqual(None, result)

        # try adding same reader
        result2 = self.library2.add_reader("reader1")
        self.assertEqual({"reader1": []}, self.library2.readers)
        self.assertEqual("reader1 is already registered in the emptylibrary library.",
                         result2)

        # add reader to existing readers
        result3 = self.library1.add_reader("reader4")
        self.assertEqual({
            "reader1": [],
            "reader2": [],
            "reader3": [],
            "reader4": []
        }, self.library1.readers)
        self.assertEqual(None, result3)

    def test_rent_book_works_properly(self):
        # non existent reader:
        result1 = self.library1.rent_book("reader4", "author1", "book1")
        self.assertEqual("reader4 is not registered in the library1 Library.", result1)
        self.assertEqual({
            "reader1": [],
            "reader2": [],
            "reader3": []
        }, self.library1.readers)
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"]
        }, self.library1.books_by_authors)

        # reader present but author non-existent
        result2 = self.library1.rent_book("reader2", "author4", "book1")
        self.assertEqual("library1 Library does not have any author4's books.", result2)
        self.assertEqual({
            "reader1": [],
            "reader2": [],
            "reader3": []
        }, self.library1.readers)
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"]
        }, self.library1.books_by_authors)

        # reader and author present, but book non-existent
        result3 = self.library1.rent_book("reader2", "author1", "book4")
        self.assertEqual("""library1 Library does not have author1's "book4".""", result3)
        self.assertEqual({
            "reader1": [],
            "reader2": [],
            "reader3": []
        }, self.library1.readers)
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4", "book5"],
            "author3": ["book6"]
        }, self.library1.books_by_authors)

        # rent book when reader, author, book present
        result4 = self.library1.rent_book("reader2", "author2", "book5")
        self.assertEqual(None, result4)
        self.assertEqual({
            "reader1": [],
            "reader2": [{"author2": "book5"}],
            "reader3": []
        }, self.library1.readers)
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": ["book4"],
            "author3": ["book6"]
        }, self.library1.books_by_authors)

        # rent one more book from same author
        result5 = self.library1.rent_book("reader2", "author2", "book4")
        self.assertEqual(None, result5)
        self.assertEqual({
            "reader1": [],
            "reader2": [{"author2": "book5"}, {"author2": "book4"}],
            "reader3": []
        }, self.library1.readers)
        self.assertEqual({
            "author1": ["book1", "book2", "book3"],
            "author2": [],
            "author3": ["book6"]
        }, self.library1.books_by_authors)

        # rent book from empty library
        self.library2.books_by_authors = {}
        self.library2.readers = {}
        result6 = self.library2.rent_book("reader1", "author1", "book1")
        self.assertEqual("reader1 is not registered in the emptylibrary Library.", result6)
        self.assertEqual({}, self.library2.readers)
        self.assertEqual({}, self.library2.books_by_authors)


if __name__ == "__main__":
    main()

