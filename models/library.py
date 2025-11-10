from models.book import Book
import user

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def borrow(self, user_id:int, isbn:int):
        for book in self.books:
            if book.isbn == isbn:
                for user in self.users:
                    if user.user_id == user_id:
                        user.borrowed_books.append(book)
                        book.is_available == False
                        break
                    
                    
    def show_available(self):
        print("available books: ")
        for book in self.books:
            if book.available == True:
                print(book)

    def add_book(self, book: Book):
        self.books.append(book)

    def return_book(self, user_id: int, book_isbn: int):
        for i in self.books:
            if i.isbn == book_isbn:
                i. is_available = True
        for i in self.users:
            if user_id == i.user_id:
                this_user = i
        for i in this_user.borrowed_books:
            if i == book_isbn:
                this_user.borrowed_books.remove(i)

aaa = Book('abc', 'def', 123)
bbb = Book('abc1', 'def2', 456)
uuu = user.User('uuu', 111)
yyy = user.User('yyy', 222)
lll = Library()
lll.add_book(aaa)
lll.add_book(bbb)