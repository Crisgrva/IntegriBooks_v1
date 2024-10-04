from flask import request
from ..models import db, Book
from ..schemas.book_schema import BookSchema

book_schema = BookSchema()
books_schema = BookSchema(many=True)


def get_books_service():
    books = Book.query.order_by(Book.title).limit(100).all()
    books_schema = BookSchema(many=True)
    result = books_schema.dump(books)

    return result


def get_recent_books_service():
    books = Book.query.order_by(Book.id.desc()).limit(10).all()
    return books_schema.dump(books), 200


def search_books_service(query):
    books = Book.query.filter(Book.title.contains(
        query) | Book.author.contains(query)).all()
    return books_schema.dump(books), 200


def add_book_service(new_book_json):
    new_book = book_schema.load(new_book_json)
    book = Book(**new_book)
    db.session.add(book)
    db.session.commit()
    return book_schema.dump(book), 201


def delete_book_service(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted successfully"}, 200


def edit_book_service(id, book_json):
    book = Book.query.get_or_404(id)
    updated_data = book_schema.load(book_json)
    for key, value in updated_data.items():
        setattr(book, key, value)
    db.session.commit()
    return book_schema.dump(book), 200


def get_book_service(id):
    book = Book.query.get(id)
    if book is None:
        raise ValueError("Book not found")
    return book_schema.dump(book), 200
