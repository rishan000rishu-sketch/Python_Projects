

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display_books(self):

        status = 'Borrowed' if self.is_borrowed else 'Available'

        print(f'''
Title  : {self.title}
Author : {self.author}
Status : {status}
''')
        
class Library:
    def __init__(self):
        self.books = []

    def add_books(self):

        title = input('Enter title name to add: ')
        author = input('Enter author name to add: ')

        new_book = Book(title, author)

        self.books.append(new_book)

        print('Book added successfully...')

    def view_books(self):

        if len(self.books) ==0:
            print('Books not available')
            return

        print('=============Book List============')

        for index, book in enumerate(self.books, start=1):
            print(f'Book {index}')
            book.display_books()
            
    def search_books(self):

        title = input('Enter title name to search: ')

        found = False

        for book in self.books:

            if book.title.lower() == title.lower():

                print('\nBook found')
                book.display_books()

                found = True
                break
            
        if not found:
            print('Book not found!!!')

    def borrow_books(self):

        title = input('Enter title name to borrow: ')

        for book in self.books:

            if book.title.lower() == title.lower():

                if not book.is_borrowed:

                    book.is_borrowed = True

                    print('Book borrowed successfully..')

                else:
                    print('Book already borrowed!!')
                return

        print('\nBook not found!!!')

    def return_books(self):

        title = input('Enter title name to return: ')

        for book in self.books:

            if book.title.lower() == title.lower():

                if book.is_borrowed:
                    
                    book.is_borrowed = False

                    print('Book returned successfully!!')

                else:
                    print('This book is not borrowed!!')
                return
            
        print('Book not found!!!')

    def remove_books(self):

        title = input('Enter title name to remove: ')

        for book in self.books:

            if book.title.lower() == title.lower():

                self.books.remove(book)

                print('Book removed succesfully!!')
            else:
                print('Book not found!!!')

library = Library()

#=====================Menu area==================#

while True:
    print('''
1. Add Book
2. View Book
3. Search Book
4. Borrow Book
5. Return book
6. Remove book
7. Exit

''')
    
    choice = input('Enter your choice: ')
    
    if choice =='1':
        library.add_books()
    
    elif choice =='2':
        library.view_books()

    elif choice =='3':
        library.search_books()

    elif choice =='4':
        library.borrow_books()

    elif choice =='5':
        library.return_books()

    elif choice =='6':
        library.remove_books()

    elif choice =='7':
        print('\n------------------------Thank you for using Library Management System-----------------------\n')
        break

    else:
        print('Invalid choice!!!!')