from datetime import datetime


class Book:
    def __init__(self, id, title, author, total):
        self.id = id
        self.title = title
        self.author = author
        self.total = total
        self.record = []


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed = []


class BookRecord:
    def __init__(self, id, member, borrow_date=None, return_date=None):
        self.id = id
        self.member = member
        self.borrow_date = borrow_date
        self.return_date = return_date


class Sys:
    def __init__(self):
        self.books = []
        self.members = []

    def find_book(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None

    def add_book(self, id, title, author, total):
        book = self.find_book(id)
        if book:
            print('book already exist.')
        else:
            book = Book(id, title, author, total)
            self.books.append(book)

    def update_book_amount(self, id, number):
        book = self.find_book(id)
        if book:
            book.total += number
        else:
            print('book not exist.')

    def remove_book(self, id):
        book = self.find_book(id)
        if book:
            self.books.remove(book)
        else:
            print('book not exist.')

    def book_detail(self, id):
        book = self.find_book(id)
        if book:
            print(f'id : {book.id}')
            print(f'title : {book.title}')
            print(f'author : {book.author}')
            print(f'total : {book.total}')
        else:
            print('book not exist.')

    def find_member(self, id):
        for member in self.members:
            if member.id == id:
                return member
        return None

    def add_member(self, id, name):
        member = self.find_member(id)
        if member:
            print('member already exist.')
        else:
            member = Member(id, name)
            self.members.append(member)

    def show_member_borrowed(self, id):
        member = self.find_member(id)
        if member:
            if member.borrowed:
                for book_id in member.borrowed:
                    book = self.find_book(book_id)
                    print(f'title : {book.title}')
            else:
                print('no book borrowed.')
        else:
            print('member not exist.')

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member:
            print('no member exist.')
            return
        if not book:
            print('no book exist.')
            return
        if book.total < 1:
            print('not enough books available.')
            return
        borrow_date = datetime.now()  # 獲取當前日期作為借閱日期
        record = BookRecord(book_id, member_id, borrow_date=borrow_date)
        member.borrowed.append(book_id)
        book.record.append(record)
        book.total -= 1
        print(f'Book {book_id} borrowed by member {
              member_id} on {borrow_date}')

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        if not member:
            print('no member exist.')
            return
        if not book:
            print('no book exist.')
            return
        for record in book.record:
            if record.member == member_id and record.return_date is None:
                record.return_date = datetime.now()  # 獲取當前日期作為歸還日期
                member.borrowed.remove(book_id)
                book.total += 1
                print(f'Book {book_id} returned by member {
                      member_id} on {record.return_date}')
                return
        print('No matching borrow record found.')

    def display_book_records(self, book_id):
        book = self.find_book(book_id)
        if not book:
            print('book not exist.')
            return
        if not book.record:
            print('no borrow records found.')
            return
        for record in book.record:
            borrow_date = record.borrow_date.strftime(
                '%Y-%m-%d %H:%M:%S') if record.borrow_date else 'N/A'
            return_date = record.return_date.strftime(
                '%Y-%m-%d %H:%M:%S') if record.return_date else 'Not returned yet'
            print(f'Member ID: {record.member}, Borrow Date: {
                  borrow_date}, Return Date: {return_date}')
