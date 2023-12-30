from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    title = Column("title", String, primary_key=True)
    author = Column("author", String)
    isbn = Column("isbn", Integer)
    total_qty = Column("total", Integer)
    available_qty = Column("available", Integer)

    def __init__(self, title, author, isbn, total_qty, available_qty):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_qty = total_qty
        self.available_qty = available_qty

    def __repr__(self):
        return f"(Título: {self.title}\nAutor: {self.author}\nISBN: {self.isbn})"


engine = create_engine('postgresql://library_admin:library@localhost/library')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


class Library:
    def __init__(self):
        self.books = session.query(Book).all()

    def update_library(self):
        self.books = session.query(Book).all()

    def register_book(self):
        print("\nRegistrando libro...")
        title = input("Título: ")
        author = input("Autor: ")
        isbn = int(input("ISBN: "))
        qty = int(input("Cantidad: "))

        new_book = Book(title, author, isbn, qty, qty)
        # session.add(new_book)
        # session.commit()
        self.books.append(new_book)
        print("Libro registrado")
        # self.update_library()
        input("Presiona enter...")

    def search_book(self):
        print("\nBuscando libro...")
        book_to_search = input("Introduce el título, autor o isbn: ")
        result = []
        for book in self.books:
            if book_to_search in book.__str__():
                result.append(book)
        self.print_books(result)
        input("Presiona enter...")

    def lend_book(self):
        print("Prestando libro...")
        isbn_to_lend = int(input("Introduce el ISBN del libro a prestar: "))
        for book in self.books:
            if book.isbn == isbn_to_lend:
                self.print_books([book])
                if book.available_qty == 0:
                    print("Este libro no tiene unidades disponibles")
                    input("Presiona enter")
                else:
                    book.available_qty = book.available_qty - 1
                    print("Libro prestado")
                    input("Presiona enter")
                    break

    def turn_back_book(self):
        print("Devolviendo libro...")
        isbn_to_turnback = int(input("Introduce el ISBN del libro a devolver: "))
        for book in self.books:
            if book.isbn == isbn_to_turnback:
                self.print_books([book])
                book.available_qty = book.available_qty + 1
                print("Libro devuelto")
                input("Presiona enter")
                break

    def show_inventory(self):
        print("\nMostrando inventario")
        self.print_books(self.books)
        input("Presiona enter...")

    def exit(self):
        print("Cerrando programa...")
        session.add_all(self.books)
        session.commit()

    def print_books(self, books):
        print("{:<20} {:<20} {:<8} {:<8} {:<8}".format("Título", "Autor", "ISBN", "Total", "Disponibles"))
        for book in books:
            print("{:<20} {:<20} {:<8} {:<8} {:<8}".format(book.title, book.author, book.isbn, book.total_qty, book.available_qty))
        print("\n\n")
