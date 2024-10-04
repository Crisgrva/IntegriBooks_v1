from flask import Blueprint, jsonify, make_response, request, abort
from .services.book_crud import add_book_service, delete_book_service, edit_book_service, get_book_service, get_books_service, get_recent_books_service, search_books_service
from .models import db, Book
from .schemas.book_schema import BookSchema
from flasgger import swag_from

api = Blueprint('api', __name__)
book_schema = BookSchema()
books_schema = BookSchema(many=True)


@api.route('/books', methods=['GET'])
@swag_from({
    'summary': 'Get All Books in Alphabetical Order',
    'description': 'Returns all books sorted alphabetically by title.',
    'responses': {
        '200': {
            'description': 'List of books',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'author': {'type': 'string'},
                        'read': {'type': 'boolean'},
                        'cover': {'type': 'string'}
                    }
                }
            }
        },
        '204': {
            'description': 'No books found'
        }
    }
})
def get_books():
    try:
        return get_books_service()
    except:
        return make_response("", 204)


@api.route('/books/recent', methods=['GET'])
@swag_from({
    'summary': 'Get Recent Books',
    'description': 'Returns the books that have been most recently added to the library.',
    'responses': {
        '200': {
            'description': 'List of recent books',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'author': {'type': 'string'},
                        'read': {'type': 'boolean'},
                        'cover': {'type': 'string'}
                    }
                }
            }
        },
        '204': {
            'description': 'No recent books found'
        }
    }
})
def get_recent_books():
    try:
        return get_recent_books_service()
    except:
        return make_response("", 204)


@api.route('/books/search', methods=['GET'])
@swag_from({
    'summary': 'Search Books',
    'description': 'Allows searching for books by title. If no title is provided, all books are returned.',
    'parameters': [
        {
            'name': 'title',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Title of the book to search for'
        }
    ],
    'responses': {
        '200': {
            'description': 'List of found books',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'author': {'type': 'string'},
                        'read': {'type': 'boolean'},
                        'cover': {'type': 'string'}
                    }
                }
            }
        },
        '400': {
            'description': 'Bad Request. Title query parameter is required.'
        }
    }
})
def search_books():
    query = request.args.get('q')
    if not query:
        return abort(400, "Title query parameter is required.")

    try:
        return search_books_service(query)
    except:
        return make_response("", 204)


@api.route('/books', methods=['POST'])
@swag_from({
    'summary': 'Add a New Book',
    'description': 'Allows adding a new book to the library.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'author': {'type': 'string'},
                    'read': {'type': 'boolean', 'default': False},
                    'cover': {'type': 'string'}
                },
                'required': ['title', 'author']
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'The book was successfully added',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'author': {'type': 'string'},
                    'read': {'type': 'boolean'},
                    'cover': {'type': 'string'}
                }
            }
        },
        '400': {
            'description': 'Bad Request. Missing required fields.'
        }
    }
})
def add_book():
    try:
        return add_book_service(request.json)
    except:
        return abort(400, "Missing required fields.")


@api.route('/books/<int:id>', methods=['DELETE'])
@swag_from({
    'summary': 'Delete a Book',
    'description': 'Allows deleting a book from the library by its ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the book to delete'
        }
    ],
    'responses': {
        '200': {
            'description': 'Book deleted successfully'
        },
        '404': {
            'description': 'Book not found'
        }
    }
})
def delete_book(id):
    try:
        return delete_book_service(id)
    except:
        return abort(404, "Book not found.")


@api.route('/books/<int:id>', methods=['PUT'])
@swag_from({
    'summary': 'Edit a Book',
    'description': 'Allows updating the information of an existing book in the library.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the book to update'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'author': {'type': 'string'},
                    'read': {'type': 'boolean'},
                    'cover': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Book updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'author': {'type': 'string'},
                    'read': {'type': 'boolean'},
                    'cover': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Book not found'
        },
        '400': {
            'description': 'Bad Request. Missing required fields.'
        }
    }
})
def edit_book(id):
    try:
        return edit_book_service(id, request.json)
    except:
        return abort(400, "Missing required fields.")


@api.route('/books/<int:id>', methods=['GET'])
@swag_from({
    'summary': 'Get a Book by ID',
    'description': 'Returns the details of a book by its ID.',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the book to retrieve'
        }
    ],
    'responses': {
        '200': {
            'description': 'Details of the book',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'author': {'type': 'string'},
                    'read': {'type': 'boolean'},
                    'cover': {'type': 'string'}
                }
            }
        },
        '404': {
            'description': 'Book not found'
        }
    }
})
def get_book(id):
    try:
        return get_book_service(id)
    except:
        abort(404)
