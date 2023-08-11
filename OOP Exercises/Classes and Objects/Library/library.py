from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        for writer in self.books_available:
            if writer == author and book_name in self.books_available[writer]:
                self.books_available[writer].remove(book_name)

                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}

                self.rented_books[user.username][book_name] = days_to_return
                user.books.append(book_name)

                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user in self.rented_books:
            for book in self.rented_books[user]:
                if book == book_name:
                    to_return = self.rented_books[user][book]
                    return f"The book \"{book_name}\" is already rented and will be available in {to_return} days!"

    def return_book(self, author: str, book_name:str, user: User) -> None or str:
        if book_name in user.books:
            user.books.remove(book_name)

            if author not in self.books_available:
                self.books_available[author] = []

            self.books_available[author].append(book_name)

            if user.username in self.rented_books and book_name in self.rented_books[user.username]:
                del self.rented_books[user.username][book_name]

        else:
            return f"{user.username} doesn't have this book in his/her records!"
