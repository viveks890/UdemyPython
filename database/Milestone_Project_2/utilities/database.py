"""
This will store the data and contains helper functions
"""
import typing

books = []

def add_book(title: str, author: str, read: bool = False) -> typing.Dict[str,bool]:
    book = {"title":title, "author":author, "read":read}
    return books.append(book)

def read_book(name: str)-> None:
    for book_name in books:
        if name == book_name["title"]:
            books["read"] = True
        else:
            print(f"{name} book doesn't exist in database")

def list_books():
    for book in books:
        print(book["name"])

def delete_book(name: str):
    books = [book for book in books if book != name]
    return books